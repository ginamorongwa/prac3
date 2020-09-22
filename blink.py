# import the module and check if it is successful
try:
	import RPi.GPIO as GPIO
except RuntimeError:
	print("Error importing RPi.GPIO! This is probably because you need superuser privileges. You can achieve this by using 'sudo' to run your script")

import time

led = 18
button = 16

def set():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	GPIO.setup(led, GPIO.OUT)
	GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def end():
	GPIO.output(led, False)
	GPIO.cleanup()

def buttonCallback(channel):
	if GPIO.input(button) == False:
		GPIO.output(led, True)
	else:
		GPIO.output(led, False)

def main():
	GPIO.add_event_detect(button, GPIO.BOTH, callback=buttonCallback)
	a = input("Press enter to quit\n\n")

if __name__ == "__main__":
	set()
	main()
	end()
