# blueprints/__init__.py
from pprint import pprint
import platform
import psutil
import json
from flask import Flask, jsonify
import requests

from flask import Blueprint
routes = Blueprint('routes', __name__)
from .consulinfo import *
from .raftpeers import *
from .sysinfo import *
from .status import *
from .services import *
