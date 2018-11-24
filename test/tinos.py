#!/usr/bin/env python
import RPi.GPIO as GPIO
import numpy as np
import time
import random

pins = [15, 16, 18, 19, 21, 22, 23,29]

MotorPin1   = 11    # pin11
MotorPin2   = 12    # pin12
MotorEnable = 13    # pin13

def setup():
	GPIO.setmode(GPIO.BOARD)          # Numbers GPIOs by physical location
	GPIO.setup(MotorPin1, GPIO.OUT)   # mode --- output
	GPIO.setup(MotorPin2, GPIO.OUT)
	GPIO.setup(MotorEnable, GPIO.OUT)
	GPIO.output(MotorEnable, GPIO.LOW) # motor stop
	for pin in pins:
            GPIO.setup(pin, GPIO.OUT)   # Set all pins' mode is output
            GPIO.output(pin, GPIO.HIGH) # Set all pins to high(+3.3V) to off led

def ch_led(curval):
    led_choice = pins[np.random.choice(len(pins))]
    GPIO.output(curval, GPIO.HIGH)
    GPIO.output(led_choice, GPIO.LOW)
    return led_choice

def ch_flora(status):
    if status == "breakF":
        GPIO.output(MotorEnable, GPIO.HIGH)
        GPIO.output(MotorPin1, GPIO.HIGH)
        GPIO.output(MotorPin2, GPIO.LOW)
        return "forwards"
    elif status == "breakB":
        GPIO.output(MotorEnable, GPIO.HIGH)
        GPIO.output(MotorPin1, GPIO.LOW)
        GPIO.output(MotorPin2, GPIO.HIGH)
        return "backwards"
    elif status == "forwards" or status == "backwards":
        GPIO.output(MotorEnable, GPIO.LOW)
    else:
        raise ValueError("ALARM unknown status")
    return "breakF" if status == "backwards" else "breakB"

def loop(flora_interval = 0.6, flora_duration = 2, led_interval = 0.2):
    led = pins[np.random.choice(len(pins))]
    flora_status = "breakF"
    flora_next_s = 0
    for s in np.arange(0,100,0.1):
        # led_switch
        if np.isclose(s%led_interval, 0):
            print("LED timepoint %f"%s)
            led = ch_led(led)
        if np.isclose(flora_next_s, s):
            print("Flora timepoint %f"%s)
            flora_status = ch_flora(flora_status)
            flora_add = flora_duration if flora_status.endswith("wards") else flora_interval
            flora_next_s = s+flora_add
        time.sleep(0.1)

def destroy():
	# GPIO.output(MotorEnable, GPIO.LOW) # motor stop
    	for pin in pins:
    		GPIO.output(pin, GPIO.HIGH)    # turn off all leds
        GPIO.output(MotorEnable, GPIO.LOW) # motor stop
        GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
