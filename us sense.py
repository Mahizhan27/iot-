import RPi.GPIO as GPIO
import time
import sqlite3

# GPIO setup for HC-SR04
GPIO.setmode(GPIO.BCM)  # Broadcom pin numbering
TRIG = 17  # GPIO pin connected to Trigger
ECHO = 27  # GPIO pin connected to Echo

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# Database setup (SQLite)
def create_database():
    # Connect to SQLite (it will create the file if it doesn't exist)
    conn = sqlite3.connect('sensor_data.db')
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS distance_readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            distance REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

# Function to measure distance using ultrasonic sensor
def measure_distance():
    # Send pulse to trigger
    GPIO.output(TRIG, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG, GPIO.LOW)

    # Wait for echo to return
    while GPIO.input(ECHO) == GPIO.LOW:
        pulse_start = time.time()

    while GPIO.input(ECHO) == GPIO.HIGH:
        pulse_end = time.time()

    # Calculate distance in cm
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # Speed of sound is 34300 cm/s, divided by 2 for round trip
    distance = round(distance, 2)

    return distance

# Function to store data in the database
def store_data(distance):
    # Connect to the database
    conn = sqlite3.connect('sensor_data.db')
    cursor = conn.cursor()

    # Insert the distance reading into the database
    cursor.execute("INSERT INTO distance_readings (distance) VALUES (?)", (distance,))

    conn.commit()
    conn.close()

    print(f"Data stored: Distance = {distance} cm")

# Main program loop
def main():
    # Create database and table if they don't exist
    create_database()

    try:
        while True:
            distance = measure_distance()  # Measure the distance
            print(f"Measured distance: {distance} cm")
            store_data(distance)  # Store the distance in the database
            time.sleep(1)  # Wait for 1 second before taking the next reading

    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()  # Cleanup GPIO pins

if __name__ == '__main__':
    main()

