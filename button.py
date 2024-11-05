mport time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
# determines the gpio numbering scheme to be used in the script
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.IN)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
while GPIO.input(18)==1:
    if GPIO.input(18)==0:
        #Setting gpios as outputs
        GPIO.output(5, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(5, GPIO.LOW)
        GPIO.output(17, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(17, GPIO.LOW)
        GPIO.output(19, GPIO.HIGH)
        time.sleep(4)
        GPIO.output(19, GPIO.LOW)
        time.sleep(2)
        break
    
