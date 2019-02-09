from flask import Flask, jsonify, request, render_template, redirect, Response, Blueprint

views = Blueprint('views', __name__, url_prefix='', template_folder='templates')

@views.route('/home', methods = ['GET'])
def home():
    return render_template("home.html")

@views.route('/metrics', methods = ['GET'])
def metrics():
    return render_template("metrics.html")

@views.route('/stream', methods = ['GET'])
def streamer():
    return render_template('streamer.html')

@views.route('/recognise', methods = ['GET'])
def recogniser():
    return render_template('recognizer.html')
