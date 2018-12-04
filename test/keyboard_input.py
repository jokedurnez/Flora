#!/usr/bin/env python

import sys
import os
sys.path.append(os.path.abspath("../app/"))
from flora import motor, poller
import RPi.GPIO as GPIO
import time

def run_flora():
    keydict = {
            "a": "left",
            "d": "right",
            "w": "forward",
            "x": "backward",
            "s": "stop"
        }
    with poller.KeyPoller() as pr:
        while True:
            key = pr.poll()
            if key is None:
                continue
            if key in keydict.keys():
                print(key)
                motor.action(keydict[key])
            else:
                print("Key unknown: %s"%key)

# while 1:
#     for dc in range(0, 101, 5):
#         p.ChangeDutyCycle(dc)
#         time.sleep(0.1)
#     for dc in range(100, -1, -5):
#         p.ChangeDutyCycle(dc)
#         time.sleep(0.1)
# p.stop()

if __name__ == '__main__':     # Program start from here
    motor.setup()
    try:
        run_flora()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        motor.destroy()
