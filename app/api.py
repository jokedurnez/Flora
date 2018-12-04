from flask import Flask, jsonify, request, render_template, redirect, Response
from clarifai.rest import ClarifaiApp
from flora import motor, metrics
from flora.utils import metrics_utils
from datetime import datetime
from picamera import PiCamera
from sqlalchemy import create_engine
import statistics

import json
import sys

with open('../secrets.json') as f:
    secrets = json.load(f)


####
## init
####

# motors
motor.setup()
# accelerometer
accel = metrics.Adafruit_ADXL345()
# object recognition
app = ClarifaiApp(api_key=secrets['CLARIFAI_API_KEY'])
model = app.public_models.general_model
# app
app = Flask(__name__)
app.config['DEBUG'] = True

####
## MOVE API
####

@app.route('/api/move/forward', methods=['GET'])
def forward():
    motor.action("forward")
    return redirect('/')

@app.route('/api/move/backward', methods=['GET'])
def backward():
    motor.action("backward")
    return redirect('/')

@app.route('/api/move/stop', methods=['GET'])
def stop():
    motor.action("stop")
    return redirect('/')

@app.route('/api/move/left', methods=['GET'])
def left():
    motor.action("left")
    return redirect('/')

@app.route('/api/move/right', methods=['GET'])
def right():
    motor.action("right")
    return redirect('/')

@app.route('/api/move/setup',methods=['GET'])
def setup():
    motor.setup()
    return redirect('/')

@app.route('/api/move/cleanup',methods=['GET'])
def cleanup():
    motor.destroy()
    return redirect('/')

@app.route('/api/move/reset',methods=['GET'])
def reset():
    motor.destroy()
    motor.setup()
    return redirect('/')

####
## FEEL API
####

@app.route('/api/feel/read',methods=['GET'])
def read():
    return accel.read()

@app.route('/api/feel/read20',methods=['GET'])
def read20():
    engine = create_engine("postgresql://pi:raspberry@localhost/flora")
    conn = engine.connect()
    command = "SELECT * FROM metrics;"
    metrics = conn.execute(command).fetchall()
    print(metrics[-1])
    outdict = metrics_utils.preprocess_metrics(metrics)
    return jsonify(outdict)

@app.route('/api/feel/readeasy',methods=['GET'])
def readeasy():
    x = [1,20,40,60,80,100]
    y = [5,10,5,20,40,60]

    out = [{"x":x, "y":y} for x,y in zip(x,y)]
    out = {"x": x, "y": y}
    # response = Response(json.load(out))
    # response.headers.add('Access-Control-Allow-Origin', "*")

    return jsonify(out)


####
## VIEWER API
####

@app.route('/api/see/shoot',methods=['GET'])
def take_picture(filename=None):
    if not isinstance(filename, str):
        date = datetime.now()
        filename = "/home/pi/pictures/pic_%s.jpg"%date
        my_file = open(filename, 'wb')
    camera = PiCamera()
    camera.start_preview()
    sleep(2)
    camera.capture(my_file)
    my_file.close()
    return redirect('/')

@app.route('/api/see/recognize/<filename>',methods=['GET'])
def recognize_picture(filename):
    prediction = model.predict_by_filename(filename)
    concepts = prediction['outputs'][0]['data']['concepts']
    conceptnames = [x['name'] for x in concepts]
    return redirect('/')

####
## HTML
####

@app.route('/home', methods = ['GET'])
def home():
    return render_template("home.html")


@app.route('/metrics', methods = ['GET'])
def metrics():
    return render_template("metrics.html")


app.add_url_rule('/', 'home', home)
