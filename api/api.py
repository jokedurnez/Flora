from flask import Flask, jsonify, request
import RPi.GPIO as GPIO
import random
import time
# see https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask

pins = {
    "output": {
        1: {"pin":15},
        2: {"pin":16},
        3: {"pin":18},
        4: {"pin":19},
        5: {"pin":21},
        6: {"pin":22},
        7: {"pin":23},
        8: {"pin":29}
        },
    "input": {}
}

GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
for led,pin in pins['output'].items():
    GPIO.setup(pin['pin'], GPIO.OUT)   # Set LedPin's mode is output
    GPIO.output(pin['pin'], GPIO.HIGH) # Set LedPin high(+3.3V) to off led
for led,pin in pins['input'].items():
    GPIO.setup(pin['pin'], GPIO.IN, pull_up_down=GPIO.PUD_UP)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Flora !</h1><p>Bladibla.</p>"

@app.route('/api/led/<int:ledpin>/on',methods=['GET'])
def led_on(ledpin):
    GPIO.output(pins['output'][ledpin]['pin'], GPIO.LOW)  # led on
    return jsonify({"response": 0})

@app.route('/api/led/<int:ledpin>/off',methods=['GET'])
def led_off(ledpin):
    GPIO.output(pins['output'][ledpin]['pin'], GPIO.HIGH)  # led on
    return jsonify({"response": 0})

@app.route('/api/led/random',methods=['GET'])
def led_random():
    for k in range(20):
        id = random.randint(1,8)
        if k != 0:
            led_off(previous)
        led_on(id)
        time.sleep(0.1)
        previous = id
    return jsonify({"response": 0})

@app.route('/api/cleanup',methods=['GET'])
def cleanup():
    for led,pin in pins['output'].items():
        GPIO.output(pin['pin'], GPIO.HIGH)
    GPIO.setup(pins['input']['button']['pin'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.cleanup()
    return jsonify({"response": 0})
