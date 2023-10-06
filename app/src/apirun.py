#!/usr/bin/python3 -u
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from pprint import pprint
import platform
import psutil
import requests
import json
from flask import Flask
from routes import *
from config.config import *

app = Flask(__name__)
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
