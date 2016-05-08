import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
INPUT_PIN = 27
GPIO.setup(27, GPIO.IN)

while 1:
	print GPIO.input(27)
		time.sleep(1)

