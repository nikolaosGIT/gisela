import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT) # Positive
GPIO.setup(24, GPIO.OUT) # Negative
# 3x pump on, pump off
for i in range(3):
    GPIO.output(23,True)
    GPIO.output(24,True)
    time.sleep(3)
    GPIO.output(23,False)
    GPIO.output(24,False)
    time.sleep(3)
GPIO.cleanup()
