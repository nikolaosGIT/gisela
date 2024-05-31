#!/usr/bin/python3

def activate(seconds):
	import RPi.GPIO as GPIO
	import time
	from datetime import datetime
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(23, GPIO.OUT) # Positive
	GPIO.setup(24, GPIO.OUT) # Negative
	# Pump on
	now = datetime.now()
	current = now.strftime("%H:%M:%S %Y:%m:%d")
	print("System online at", current)
	#GPIO.output(23,True)
	#GPIO.output(24,True)
	# Keep on for 3 seconds
	time.sleep(seconds)
	# Pump off
	now = datetime.now()
	current = now:strftime("%H:%M:%S %Y:%m:%d")
	print("System offline at", current)
	#GPIO.output(23,False)
	#GPIO.output(24,False)
	GPIO.cleanup()

if __name__ == '__main__':
	activate(1)
