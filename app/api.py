from flask import Flask, jsonify, request, render_template, redirect

import sys

from flora import motor

motor.setup()

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/api/forward', methods=['GET'])
def forward():
    motor.action("forward")
    return redirect('/')

@app.route('/api/backward', methods=['GET'])
def backward():
    motor.action("backward")
    return redirect('/')

@app.route('/api/stop', methods=['GET'])
def stop():
    motor.action("stop")
    return redirect('/')

@app.route('/api/left', methods=['GET'])
def left():
    motor.action("left")
    return redirect('/')

@app.route('/api/right', methods=['GET'])
def right():
    motor.action("right")
    return redirect('/')

@app.route('/api/setup',methods=['GET'])
def setup():
    motor.setup()
    return redirect('/')

@app.route('/api/cleanup',methods=['GET'])
def cleanup():
    motor.destroy()
    return redirect('/')

@app.route('/home', methods = ['GET'])
def home():
    return render_template("home.html")

app.add_url_rule('/', 'home', home)
