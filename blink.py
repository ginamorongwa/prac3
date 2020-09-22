# import the module and check if it is successful
try:
	import RPi.GPIO as GPIO
except RuntimeError:
	print("Error importing RPi.GPIO! This is probably because you need superuser privileges. You can achieve this by using 'sudo' to run your script")

import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

def main():
	print("LED ON")
	GPIO.output(18, GPIO.HIGH)
	time.sleep(20)
	print("LED OFF")
	GPIO.output(18, GPIO.LOW)

if __name__ == "__main__":
	main()
