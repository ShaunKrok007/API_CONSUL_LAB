# blueprints/raftpeers.py
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

@routes.route('/raftpeers', methods=['GET'])
def get_raft_peers():
    try:
        response = requests.get(f'{CONSUL_API_URL}/v1/operator/raft/configuration')
        data = response.json()
        json_data = json.dumps(data, indent=2)
        logging.info(json_data)
        # Set the response content type to JSON
        response = app.response_class(
            response=json_data,
            status=200,
            mimetype='application/json'
        )
        return response
    except requests.exceptions.RequestException as err:
        return jsonify({"error": str(err)})
