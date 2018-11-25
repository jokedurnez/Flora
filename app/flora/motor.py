#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

pins = {
    "drive": {
        1: 13,
        2: 11,
        "c": 7
        },
    "direction": {
        1: 22,
        2: 18,
        "c": 16
    }
}

allpins = [v for key,side in pins.items() for k,v in side.items()]
controlpins = [v for key,side in pins.items() for k,v in side.items() if k=='c']

def backward():
    GPIO.output(pins['drive']['c'], GPIO.HIGH)
    GPIO.output(pins['drive'][1], GPIO.HIGH)
    GPIO.output(pins['drive'][2], GPIO.LOW)

def forward():
    GPIO.output(pins['drive']['c'], GPIO.HIGH)
    GPIO.output(pins['drive'][1], GPIO.LOW)
    GPIO.output(pins['drive'][2], GPIO.HIGH)

def stop():
    GPIO.output(pins['drive']['c'], GPIO.LOW)

def turn(direction, scale=1, freq=1, dc=50, dur=0.05):
    dir1 = 1 if direction == "left" else 2
    dir2 = 2 if direction == "left" else 1
    GPIO.output(pins['direction'][dir1], GPIO.LOW)
    GPIO.output(pins['direction'][dir2], GPIO.HIGH)
    p = GPIO.PWM(pins['direction']['c'], freq)
    p.start(dc)
    time.sleep(dur*scale)
    p.stop()
    GPIO.output(pins['direction']['c'], GPIO.LOW)
    GPIO.output(pins['direction'][dir1], GPIO.LOW)
    GPIO.output(pins['direction'][dir2], GPIO.LOW)

def stop_rotation():
    GPIO.output(pins['direction']['c'], GPIO.LOW)

def action(action, **kwargs):
    if action == "left":
        turn("left",**kwargs)
    if action == "right":
        turn("right",**kwargs)
    if action == "forward":
        forward()
    if action == "backward":
        backward()
    if action == "stop":
        stop()

def setup():
    GPIO.setmode(GPIO.BOARD)
    for pin in allpins:
        GPIO.setup(pin, GPIO.OUT)
    for controlpin in controlpins:
        GPIO.output(controlpin, GPIO.LOW)


def loop():
    while True:
        print ('Press Ctrl+C to end the program...')
        turn("left")
        backward()
        time.sleep(2)

        stop()
        time.sleep(0.2)

        turn("right")
        forward()
        time.sleep(2)

        stop()
        time.sleep(0.2)



def destroy():
    stop()
    GPIO.cleanup()                     # Release resource
