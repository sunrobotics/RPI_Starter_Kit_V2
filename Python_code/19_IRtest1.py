#!/usr/bin/python
###########################################################################
#Filename      : 19_IRtest1.py
#Description   : BMP180 test code
#Company       : SunRobotics Technologies
#Website       : www.sunrobotics.co.in
#E-mail        : support@sunrobotics.co.in(For Any Query)
############################################################################

"""
$      If KEY_1 is pressed,this script will be executed,LED1 will turn on(or off)
$      LED1 connect to GPIO5(BCM_GPIO 24)
"""
import RPi.GPIO as GPIO

PIN = 24

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(PIN, GPIO.IN)
GPIO.setup(PIN, GPIO.OUT)

if GPIO.input(PIN) == 0:
     GPIO.output(PIN, GPIO.HIGH)
else:
     GPIO.output(PIN, GPIO.LOW)
