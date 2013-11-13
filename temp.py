#! /usr/bin/python


# This is a test module for the RaspberryPi programmable thermostat
# project. This module prepares and reads the temperature from a couple 
# of DS18B20 1-wire digital sensors

import os # we need this to load the 1-wire kernel modules

# Start by loading the kernel modules for 1-wire interface and sensors
os.system('sudo modprobe w1-gpio')
os.system('sudo modprobe w1-therm')

# Setup the 1-wire address of each sensor
# NB: To find the addres, connect the sensors and run the two modprobe
# commands from lines 11 & 12 above.
# Navigate to '/sys/bus/w1/devices'dir and type 'ls'. You should see
# the DS18B20 devices listed as 28-........... this is the file
# address for each sensor. You can add as many as you like, just
# connect them in parallel and the 1-wire module handles the calls


sense1 = "/sys/bus/w1/devices/28-000004d428de/w1_slave"
sense2 = "/sys/bus/w1/devices/28-000004d3f8b3/w1_slave"


def getTemp(sense1, sense2):
	"Read two DS18B20 temperature sensors and retun two values"

	# First we open both sensors as files
	t1file = open(sense1)
	t2file = open(sense2)

	# Read the values into strings and close the file
	text1 = t1file.read()
	text2 = t2file.read()
	t1file.close()
	t2file.close()

	# Extract the temperatures from the end of the 2nd line
	temp1 = text1.split("\n")[1].split(" ")[9]
	temp2 = text2.split("\n")[1].split(" ")[9]
	
	# Convert the 12-bit temperature to a conventional decimal
	T1 = float((temp1[2:]))/1000
	T2 = float((temp2[2:]))/1000
	
	return T1, T2 # return the two temperatures


while(1):
	
	# An endless test loop to fetch and print temperatures
	# hit Ctl-C in the terminal to exit
	
	temp1, temp2 = getTemp(sense1, sense2)
	
	print temp1, temp2 # print the result
	
	
