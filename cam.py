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
        env = os.environ
        env['LD_LIBRARY_PATH'] = stream_dir
        command = "./camstream/mjpg_streamer -i './camstream/input_uvc.so' -o './camstream/output_http.so -w ./camstream/www'"
        subprocess.Popen(command, shell=True, env=env)

cam = Cam()
