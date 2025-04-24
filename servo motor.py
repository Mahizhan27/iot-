import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
p=GPIO.PWM(11,50)
p.start(0)
for i in range(int(input('enter the num:'))):
    p.ChangeDutyCycle(1)
    sleep(1)
    p.ChangeDutyCycle(25)
    sleep(1)
p.stop()
GPIO.cleanup()