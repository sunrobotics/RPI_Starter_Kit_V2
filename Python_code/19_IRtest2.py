#!/usr/bin/python
###########################################################################
#Filename      : 19_IRtest2.py
#Description   : BMP180 test code
#Company       : SunRobotics Technologies
#Website       : www.sunrobotics.co.in
#E-mail        : support@sunrobotics.co.in(For Any Query)
############################################################################

"""
$      If KEY_2 is pressed,this script will be executed,LED1 will turn on(or off)
$      LED2 connect to GPIO6(BCM_GPIO 25)
"""
import RPi.GPIO as GPIO

PIN = 25

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(PIN, GPIO.IN)
GPIO.setup(PIN, GPIO.OUT)

if GPIO.input(PIN) == 0:
     GPIO.output(PIN, GPIO.HIGH)
else:
     GPIO.output(PIN, GPIO.LOW)
