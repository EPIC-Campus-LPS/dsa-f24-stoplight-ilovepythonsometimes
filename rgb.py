import time
import RPi.GPIO as GPIO

while True:
    
    GPIO.setmode(GPIO.BCM)
    # determines the gpio numbering scheme to be used in the script
    GPIO.setwarnings(False)
    #sets it so that warnings dont activate
    GPIO.setup(19, GPIO.OUT)
    print("Red light")
    GPIO.output(19, GPIO.HIGH)
    time.sleep(4)
    GPIO.output(19, GPIO.LOW)
    
    GPIO.setup(5, GPIO.OUT)
    print("Green light")
    #Setting gpios as outputs
    GPIO.output(5, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(5, GPIO.LOW)
    
    GPIO.output(5, GPIO.HIGH)
    GPIO.output(19, GPIO.HIGH)
    print("Yellow light")
    time.sleep(1)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(5, GPIO.LOW)
