# blueprints/status.py
#!/usr/bin/python3 -u
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
import json
from flask import Flask, jsonify
from . import routes
import requests
from config.config import *

app = Flask(__name__)

@routes.route('/status', methods=['GET'])
def check_status():
    try:
        # Define the URL of the Consul server you want to check
        response = requests.get(f'{CONSUL_API_URL}/v1/status/leader')
        data = response.json()
        if response.status_code == 200:
            print(data, flush=True)
            message = ({"status": "1", "message": "Consul server is running"})
            print(message, flush=True)
            return jsonify({"status": "1", "message": "Consul server is running"})
        return jsonify({"status": "0", "message": "Consul server is not running"})
    except requests.exceptions.RequestException as err:
        return jsonify({"status": "0", "message": f"Error: {str(err)}"})

