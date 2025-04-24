import sqlite3

# Function to fetch data from the database
def fetch_data():
    conn = sqlite3.connect('sensor_data.db')
    cursor = conn.cursor()

    # Query to fetch all distance readings and their timestamps
    cursor.execute("SELECT id, distance, timestamp FROM distance_readings")

    # Fetch all rows from the result
    rows = cursor.fetchall()

    # Display the fetched data
    if rows:
        print("ID | Distance (cm) | Timestamp")
        print("-----------------------------------")
        for row in rows:
            print(f"{row[0]} | {row[1]} cm | {row[2]}")
    else:
        print("No data found.")

    conn.close()

# Example usage:
if __name__ == '__main__':
    fetch_data()
