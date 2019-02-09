from flask import Flask, jsonify, request, render_template, redirect, Response
from clarifai.rest import ClarifaiApp
from flora import motor, metrics, camera
from flora.metrics_functions import utils, Adafruit_ADXL345
from datetime import datetime
from picamera import PiCamera
from sqlalchemy import create_engine
from api import api
from views import views, home, metrics, streamer
import statistics
import threading
import time
import json
import sys


####
## init
####

# motors
motor.setup()
# app
app = Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(views)
app.config['DEBUG'] = True
app.config['MEDIADIR'] = "/home/pi/flora/app/static/img/"

app.add_url_rule('/', 'home', home)
app.add_url_rule('/', 'metrics', metrics)
app.add_url_rule('/', 'stream', streamer)
