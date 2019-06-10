#!/usr/bin/python3

import RPi.GPIO as GPIO
from time import sleep
import random

#Referring to pins set to by Pin Number
GPIO.setmode(GPIO.BOARD)
#Output for PWM Signal to be sent on
GPIO.setup(05, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
#PWM set on pin #5 at 50Hz
tilt = GPIO.PWM(05,50)
pan = GPIO.PWM(16, 50)
#Start with 0 Duty Cycle so no angle on startup
tilt.start(0)
pan.start(0)

def tiltAngle(angle):
	#i.e. 90 degrees = 90/18 +2 = 7% Duty
	duty = angle / 18 + 2
	global tAngle
	tAngle = angle
	global tDuty
	tDuty= duty
	#Turn on Pin 05 for Output
	GPIO.output(05, True)
	#Change Duty Cycle to the angle we set
	tilt.ChangeDutyCycle(duty)
	#Give Servo time to turn
	sleep(1)
	#Turn Pin 05 Off
	GPIO.output(05, False)
	#Set Angle back to 0 so we don't continuously send inputs to servo
	tilt.ChangeDutyCycle(0)

def panAngle(angle):
	duty = angle / 18 + 2
	global pAngle
	pAngle = angle
	global pDuty
	pDuty = duty
	GPIO.output(16, True)
	pan.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(16, False)
	pan.ChangeDutyCycle(0)

def finish():
	pan.stop()
	tilt.stop()
	GPIO.cleanup()

#Custom Functions
def sweep():
	tiltAngle(30)
	list = [15,30,45,60,75,90]
	for x in range(0,6):
		panAngle(list[x])
		print(list[x])
	finish()
	exit()
def privacyMode():
	panAngle(90)
	tiltAngle(180)

def viewRoom():
	panAngle(142)
	tiltAngle(30)
def getPosition():
	print("Pan: "+str(pAngle)+" degrees, "+str(pDuty)+" duty")
	print("Tilt: "+str(tAngle)+" degrees, "+str(tDuty)+" duty")

maxAng = 180
minAng = 0
def right(spaces):
	global maxAng, minAng
	newAng = pAngle - 18 * spaces
	spaceLeft = (pAngle - minAng)/18

	if(minAng > newAng):
		#print("I can only go "+str(spaceLeft)+" more spaces!")
		panAngle(pAngle-18*spaceLeft)
	else:
		panAngle(newAng)
def left(spaces):
	global maxAng, minAng
	newAng = pAngle + 18 * spaces
	spaceLeft = (maxAng - pAngle)/18

	if(maxAng < newAng):
		#print("I can only go "+str(spaceLeft)+" more spaces!")
		panAngle(pAngle+18*spaceLeft)
	else:
		panAngle(newAng)
def up(spaces):
	global maxAng, minAng
	newAng = tAngle + 18 * spaces
	spaceLeft = (maxAng-tAngle)/18

	if(maxAng < newAng):
		#print("I can only go "+str(spaceLeft)+" more spaces!")
		tiltAngle(tAngle+18*spaceLeft)
	else:
		tiltAngle(newAng)
def down(spaces):
	global maxAng, minAng
	newAng = tAngle - 18 * spaces
	spaceLeft = (tAngle - minAng)/18

	if(minAng > newAng):
		#print("I can only go "+str(spaceLeft)+" more spaces!")
		tiltAngle(tAngle-18*spaceLeft)
	else:
		tiltAngle(newAng)

def headBang():
	phrases = ["Woo!","Yeah!","Now this is rock and roll!","Party Hard!","Awe yea!","Woooooo!!!","WOOOOO!!!!","Epic Gamer Moment!","Hardcore!","Radical","AWEssomeee!!"]
	for x in range(0,10):
		up(1000)
		down(1000)
		print(random.choice(phrases))

#position both at 90 degrees
tiltAngle(90)
panAngle(90)

print("Functions: panAngle(angle), tiltAngle(angle), sweep(), privacyMode(), viewRoom(), getPosition(), headBang()")
print("Manual Movement: up(spaces), down(spaces), left(spaces), right(spaces)")
print("Be sure to use finish() before you leave!")
