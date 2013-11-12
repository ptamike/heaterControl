#! /usr/bin/python

import os

os.system('sudo modprobe w1-gpio') #load 1-wire interface
os.system('sudo modprobe w1-therm') # load tem module


while(1):
	"Repeatedly read and print the results from two 1-wire sensors"

	tfile = open("/sys/bus/w1/devices/28-000004d428de/w1_slave")
	t1file = open("/sys/bus/w1/devices/28-000004d3f8b3/w1_slave")

	text = tfile.read()
	text1 = t1file.read()
	tfile.close()
	t1file.close()

	temp = text.split("\n")[1].split(" ")[9]
	temp1 = text1.split("\n")[1].split(" ")[9]
	T = float((temp[2:]))/1000
	T1 = float((temp1[2:]))/1000
	
	print T, "C :: ", T1, "C  "
	
