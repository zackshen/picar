#coding=utf-8

import os
import sys

cur_dir = os.path.dirname(__file__)
sys.path.append(cur_dir)

from flask import Flask, jsonify
from flask import render_template
from car import car
from cam import cam

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", name='Maker')

@app.route('/car/forward', methods=['POST'])
def car_forward():
    try:
        car.forward()
        return jsonify(**{'ok': True})
    except Exception, e:
        return jsonify(**{'ok': False, 'error': str(e)})

@app.route('/car/backward', methods=['POST'])
def car_backward():
    try:
        car.backward()
        return jsonify(**{'ok': True})
    except Exception, e:
        return jsonify(**{'ok': False, 'error': str(e)})


@app.route('/car/turnleft', methods=['POST'])
def car_turn_left():
    try:
        car.turn_left()
        return jsonify(**{'ok': True})
    except Exception, e:
        return jsonify(**{'ok': False, 'error': str(e)})


@app.route('/car/turnright', methods=['POST'])
def car_turn_right():
    try:
        car.turn_right()
        return jsonify(**{'ok': True})
    except Exception, e:
        return jsonify(**{'ok': False, 'error': str(e)})

@app.route('/car/stop', methods=['POST'])
def car_stop():
    try:
        car.stop()
        return jsonify(**{'ok': True})
    except Exception, e:
        return jsonify(**{'ok': False, 'error': str(e)})


@app.route('/cam/left', methods=['POST'])
def cam_left():
    try:
        cam.left()
        return jsonify(**{'ok': True})
    except Exception, e:
        return jsonify(**{'ok': False, 'error': str(e)})

@app.route('/cam/right', methods=['POST'])
def cam_right():
    try:
        cam.right()
        return jsonify(**{'ok': True})
    except Exception, e:
        return jsonify(**{'ok': False, 'error': str(e)})

@app.route('/cam/up', methods=['POST'])
def cam_up():
    try:
        cam.up()
        return jsonify(**{'ok': True})
    except Exception, e:
        return jsonify(**{'ok': False, 'error': str(e)})

@app.route('/cam/down', methods=['POST'])
def cam_down():
    try:
        cam.down()
        return jsonify(**{'ok': True})
    except Exception, e:
        return jsonify(**{'ok': False, 'error': str(e)})

@app.route('/cam/stop', methods=['POST'])
def cam_stop():
    try:
        cam.stop()
        return jsonify(**{'ok': True})
    except Exception, e:
        return jsonify(**{'ok': False, 'error': str(e)})

if __name__ == '__main__':
    import RPi.GPIO as GPIO
    try:
        cam.setup()
        app.run(host='0.0.0.0', port=8899)
    except:
        GPIO.cleanup()
