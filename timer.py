#! /usr/bin/python

import datetime
import time

"""This is a test module for the heater control. The function timerCheck returns the programmed temperature
based on the settings in onTime, offTime, tempOn and tempOff this return value can then be used with temp.py
module to determine whether the heater should be turned on."""

onTime = 8 
offTime = 21
tempOn = 18.5 # sets the on temperature
tempOff = 5 # sets the off temperature


def timerCheck(onTime, offTime):
	"Gets the time and sets temperature according to schedule"
	
	now = datetime.datetime.now() # get the current time
	hour = now.hour # extract the hour
	if onTime <= hour<= offTime: # decide temperature to use
		tempRqd = tempOn
	else:
		tempRqd = tempOff
		
	return (tempRqd)

while(1):
	tempRqd = timerCheck(onTime, offTime)	
	print tempRqd
	

