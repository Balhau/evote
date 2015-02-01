__author__ = 'balhau'
from flask import Flask
from flask import request
from flask import render_template
import subprocess,shlex,json,os,signal
from os import listdir
from os.path import isfile, join


app=Flask(__name__)

omxProcess=None

@app.route('/')
def index():
	return render_template('index.html')


if __name__ == '__main__':
	app.debug=True
	app.run(host='0.0.0.0')
