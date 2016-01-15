#!/usr/bin/python
import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BOARD)
gpio.setup(7,gpio.OUT)
gpio.output(7,1)

print "hello world"

time.sleep(5)

gpio.output(7,0)

gpio.cleanup()
