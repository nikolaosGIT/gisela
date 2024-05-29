import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(23, GPIO.OUT)
# loop through 50 times, on/off for 1 second
for i in range(10):
    GPIO.output(7,True)
    time.sleep(1)
    GPIO.output(7,False)
    time.sleep(1)
GPIO.cleanup()