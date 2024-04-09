import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
###########################
GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(27, GPIO.IN)
GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)

def Cam_On():
    GPIO.output(26, GPIO.HIGH)  # Turn on

def Cam_Off():
    GPIO.output(26, GPIO.LOW)  # Turn off

def communication_on():
    GPIO.output(19, GPIO.HIGH)  # Turn on


def communication_off():
    GPIO.output(19, GPIO.LOW)  # Turn off


def ADCS_on():
    GPIO.output(13, GPIO.HIGH)  # Turn on


def ADCS_off():
    GPIO.output(13, GPIO.LOW)  # Turn off
    

def OBC_on():
    GPIO.output(6, GPIO.HIGH)  # Turn on


def OBC_off():
    GPIO.output(6, GPIO.LOW)  # Turn off


def POWER_on():
    GPIO.output(5, GPIO.HIGH)  # Turn on


def POWER_off():
    GPIO.output(5, GPIO.LOW)  # Turn off

OBC_on()
POWER_on()

ADCS_on()
Cam_On()
communication_on()

