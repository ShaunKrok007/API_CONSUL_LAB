# blueprints/__init__.py
from flask import Blueprint
routes = Blueprint('routes', __name__)
from .consulinfo import *
from .raftpeers import *
from .sysinfo import *
from .status import *
from .services import *
