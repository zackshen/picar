#coding=utf-8
import os
import subprocess
import time
import RPi.GPIO as GPIO

cur_dir = os.path.dirname(__file__)
stream_dir = os.path.join(cur_dir, 'camstream')
stream_exe = os.path.join(stream_dir, 'mjpg_streamer')
input_lib = os.path.join(stream_dir, 'input_uvc.so')
output_lib = os.path.join(stream_dir, 'output_http.so')
web_dir = os.path.join(stream_dir, 'www')

'''
0.5ms - 0deg - 2.5%
1ms - 45deg - 5%
1.5ms - 90deg - 7.5%
2ms - 135deg - 10%
2.5ms - 180deg - 12.5%
'''

ROUND_STEP = 5

GPIO.setmode(GPIO.BCM)

class Servo(object):

    def __init__(self, pin):
        self.pin = pin
        self.cur_deg = 90
        self.duty = 7.5
        self.servo = self._init()
        self.servo.start(self.duty)
        time.sleep(0.5)
        self.servo.stop()

    def _init(self):
        GPIO.setup(self.pin, GPIO.OUT)
        self.servo = GPIO.PWM(self.pin, 50)
        return self.servo

    def _go(self, start, end, reverse=False):
        delta = (12.5-2.5)/180
        for i in range(start, end, -1 if reverse else 1):
            v = round(2.5 + delta * i, 1)
            self.servo.ChangeDutyCycle(v)
            time.sleep(0.001)
            self.duty = v

    def _clear(self):
        GPIO.cleanup()

    def move_to(self, deg):
        self.servo = self._init()
        self.servo.start(self.duty)
        if deg > self.cur_deg:
            self._go(self.cur_deg, deg)
        else:
            self._go(self.cur_deg, deg, reverse=True)
        self.cur_deg = deg
        self.servo.stop()
        self._clear()

    def neutral(self):
        self.servo = self._init()
        self.servo.start(7.5)
        self.cur_deg = 90
        time.sleep(0.1)
        self.servo.stop()
        self._clear()

class HServo(Servo):

    def left(self):
        degree = self.cur_deg + ROUND_STEP
        if degree >= 180:
            degree = 180
        if self.cur_deg == degree:
            return
        self.move_to(degree)

    def right(self):
        degree = self.cur_deg - ROUND_STEP
        if degree <= 0:
            degree = 0
        if self.cur_deg == degree:
            return
        self.move_to(degree)

class VServo(Servo):

    def up(self):
        degree = self.cur_deg - ROUND_STEP
        if degree <= 0:
            degree = 0
        if self.cur_deg == degree:
            return
        self.move_to(degree)

    def down(self):
        degree = self.cur_deg + ROUND_STEP
        if degree >= 180:
            degree = 180
        if self.cur_deg == degree:
            return
        self.move_to(degree)

class Cam(object):

    def __init__(self):
        self.v_servo = VServo(6)
        self.h_servo = HServo(5)

    def setup(self):
        env = os.environ
        env['LD_LIBRARY_PATH'] = stream_dir
        command = "./camstream/mjpg_streamer -i './camstream/input_uvc.so' -o './camstream/output_http.so -w ./camstream/www'"
        subprocess.Popen(command, shell=True, env=env)

    def left(self):
        self.h_servo.left()

    def right(self):
        self.h_servo.right()

    def up(self):
        self.v_servo.up()

    def down(self):
        self.v_servo.down()

    def stop(self):
        self.v_servo.stop()
        self.h_servo.stop()

cam = Cam()
