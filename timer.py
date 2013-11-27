#! /usr/bin/python

import datetime
import time

onTime = 7 
offTime = 21
tempOn = 18.5 # sets the on temperature
tempOff = 5 # sets the off temperature


def timerCheck(onTime, offTime):
	"Gets the time and sets temperature according to schedule"
	
	now = datetime.datetime.now() # get the current time
	hour = now.hour # extract the hour
	if onTime <= hour<= offTime: # decide temperature to use
		temp = tempOn
	else:
		temp = tempOff
		
	return (temp)

while(1):
	temp = timerCheck(onTime, offTime)	
	print temp
	

