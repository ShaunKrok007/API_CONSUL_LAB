# blueprints/consulinfo.py
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

@routes.route('/consulinfo', methods=['GET'])
def get_consulinfo():
    try:
        # Get the list of nodes registered with Consul
        nodes_response = requests.get(f'{CONSUL_API_URL}/v1/catalog/nodes')
        nodescount = len(nodes_response.json())
        nodes_count = {
            "Number of Nodes": nodescount,
        }

        # Get the list of services registered with Consul
        services_response = requests.get(f'{CONSUL_API_URL}/v1/catalog/services')
        services_count = len(services_response.json())

        # Get the Consul cluster leader information
        leader_response = requests.get(f'{CONSUL_API_URL}/v1/status/leader')
        cluster_leader = leader_response.json()

        # Get the internal protocol version used by Consul
        version_response = requests.get(f'{CONSUL_API_URL}/v1/agent/self')
        consul_version = version_response.json()['Config']['Version']

        # Get the internal protocol version used by Consul
        members_response = requests.get(f'{CONSUL_API_URL}/v1/agent/members')
        consul_members_list = members_response.json()

        # Create a dictionary to store all the information
        consul_info = {
            "Nodes Count": nodes_count,
            "Services Count": services_count,
            "Cluster Leader": cluster_leader,
            "Consul Version": consul_version,
            "Consul Members": consul_members_list,
        }
        # Convert the dictionary to a JSON string with indentation
        consul_info_json = json.dumps(consul_info, indent=4)
        logging.info(consul_info_json)
        # Set the response content type to JSON
        response = app.response_class(
            response=consul_info_json,
            status=200,
            mimetype='application/json'
        )
        return response
    except requests.exceptions.RequestException as err:
        return jsonify({"error": str(err)})
