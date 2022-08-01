#!/usr/bin/env python3
import RPi.GPIO as GPIO
from time import sleep
import notify

GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(22, GPIO.IN)

pressed = False
try:
	while True:
		if GPIO.input(22):
			if not pressed:
				notify.publish_message('dash/hwr2', 'klingel')
				pressed = True
				print("LED an")
				GPIO.output(15,True)
		else:
			if pressed:
				print("LED aus")
				pressed = False
				GPIO.output(15,False)
		sleep(0.01)
except KeyboardInterrupt:
    print ('KeyboardInterrupt exception is caught')
finally:
	GPIO.cleanup()               ## Cleanup
