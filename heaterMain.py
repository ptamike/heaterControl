#! /usr/bin/python
""" A simple heating control system using a Raspberry Pi with a 1-wire digital
temperature sensor and Adafruit capacitive touch switches. At the moment the timer 
only uses the hour digit with the on and off times set by onTime and offTime. The temperature
can be set with tempOn and tempOff. tempOff is set to 5C for frost protection.
Holiday mode uses a toggle switch and forces the temperature to the off value.
The Override switch changes the required temp to the on value for one hour.
"""

import datetime
import time
import os # we need this to load the 1-wire kernel modules
import RPi.GPIO as GPIO

#Setup the GPIO pins 
GPIO.setmode(GPIO.BOARD) # Set pin numbering
GPIO.setup(11, GPIO.IN) # Holiday switch input
GPIO.setup(13, GPIO.IN) # Override switch input
GPIO.setup(15, GPIO.OUT, initial=0) # Initialise with heater off
heater = 0 #only used for testing

# Start by loading the kernel modules for 1-wire interface and sensor
os.system('sudo modprobe w1-gpio')
os.system('sudo modprobe w1-therm')


# Now pre-set the on/off time and required temperatures.
onTime = 8 
offTime = 21
tempOn = 18.5 # sets the on temperature
tempOff = 5 # sets the off temperature

# Setup the 1-wire address of each sensor

sense1 = "/sys/bus/w1/devices/28-000004d428de/w1_slave"



def timerCheck(onTime, offTime):
	"Gets the time and sets temperature according to schedule"
	
	now = datetime.datetime.now() # get the current time
	hour = now.hour # extract the hour
	if onTime <= hour<= offTime: # decide temperature to use
		tempRqd = tempOn
	else:
		tempRqd = tempOff
		
	return (tempRqd)
	
# --------------------------------------------------------------

def getTemp(sense1):
	"Read  DS18B20 temperature sensors and retun two values"

	# First we open the sensor as a file
	t1file = open(sense1)
	

	# Read the value into strings and close the file
	text1 = t1file.read()
	t1file.close()


	# Extract the temperatures from the end of the 2nd line
	temp1 = text1.split("\n")[1].split(" ")[9]
	
	# Convert the 12-bit temperature to a decimal value
	T1 = float((temp1[2:]))/1000
	
	return T1# return the current temperature



while(1): # Start a continuous loop
	tempRqd = timerCheck(onTime, offTime) #Get the programmed temp	
	print "programme Temperature: ", tempRqd
	
	if (GPIO.input(11) == True): # Check for Holiday mode
		tempRqd = tempOff
		
	print "After Holiday: ", tempRqd, GPIO.input(11)
	
	if (GPIO.input(13) == True): # Check for override
		tempRqd = tempOn
		
	print "After override: ", tempRqd, GPIO.input(13)
	
	tempNow = getTemp(sense1)
	
	print "Current Temp is: ",tempNow,"C"
	
	# Heater on/off decision
	
	if tempNow>(tempRqd+0.5): #Turn off when temp is +0.5C high
		heater = 0
		GPIO.output(15, 0)
	elif tempNow<(tempRqd-0.5): #Turn on when temp is 0.5C low
		heater = 1
		GPIO.output(15, 1)
		
	if heater == 1:
		print "Heater is ON"
	else:
		print "Heater is OFF"
	
	
	
	
	
	
GPIO.cleanup() #Tidy-up the GPIO port as we exit


