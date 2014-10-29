#coding=utf-8
import os
import subprocess

cur_dir = os.path.dirname(__file__)
stream_dir = os.path.join(cur_dir, 'camstream')
stream_exe = os.path.join(stream_dir, 'mjpg_streamer')
input_lib = os.path.join(stream_dir, 'input_uvc.so')
output_lib = os.path.join(stream_dir, 'output_http.so')
web_dir = os.path.join(stream_dir, 'www')

class Cam(object):

    def __init__(self):
        pass

    def setup(self):
        command = [
            stream_exe,
            '-i',
            input_lib,
            '-o',
            '%s -w %s' % (output_lib, web_dir)
        ]
        subprocess.Popen(command, shell=True)

cam = Cam()
