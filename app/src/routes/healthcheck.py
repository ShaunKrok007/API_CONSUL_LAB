# blueprints/healthcheck.py
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

@routes.route('/healthcheck', methods=['GET'])
def get_consul_health():
    try:
        # Send a GET request to the Consul server
        response = requests.get(f'{CONSUL_API_URL}/v1/health/state/passing')
        data_out = response.json()
        # Convert the dictionary to a JSON string with indentation
        health_data_json = json.dumps(data_out, indent=4)
        logging.info(health_data_json)
        # Set the response content type to JSON
        response = app.response_class(
            response=health_data_json,
            status=200,
            mimetype='application/json'
        )
        return response
    except requests.exceptions.RequestException as err:
        return jsonify({"error": str(err)})
