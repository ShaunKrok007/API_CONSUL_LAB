import requests
from flask import Flask, jsonify, render_template
import json
from tabulate import tabulate
from pprint import pprint
from logging.handlers import SysLogHandler
import logging
import platform
import subprocess
import psutil

app = Flask(__name__)

#CONSUL_API_URL = 'http://host.docker.internal:8500'  # Replace with your Consul server address
CONSUL_API_URL = 'http://127.0.0.1:8500'  # Replace with your Consul server address


@app.route('/systeminfo', methods=['GET'])
def get_system_info():
    # Basic system information
    system_info = {
        "Operating System": platform.system(),
        "OS Version": platform.version(),
        "Machine Architecture": platform.machine(),
        "Processor": platform.processor(),
    }

    # CPU information
    cpu_info = {
        "CPU Cores": psutil.cpu_count(logical=False),  # Physical cores
        "Logical CPUs": psutil.cpu_count(logical=True),  # Including hyperthreads
        "CPU Usage": psutil.cpu_percent(interval=1, percpu=True),
    }

    network_stats = {
        "Disk utilization": psutil.disk_usage('/'),
    }
    # Memory information
    memory_info = {
        "Total Memory (GB)": round(psutil.virtual_memory().total / (1024 ** 3), 2),
        "Available Memory (GB)": round(psutil.virtual_memory().available / (1024 ** 3), 2), 
    }

    # Get a list of all network interfaces
    network_interfaces = psutil.net_if_stats()
    
    # Prepare the data as a dictionary
    interface_data = {}
    for interface, stats in network_interfaces.items():
        interface_data[interface] = {
            'is_up': stats.isup,
            'duplex': stats.duplex,
            'mtu': stats.mtu,
            'speed': stats.speed,
        }
        
    pprint(system_info)
    pprint(cpu_info)
    pprint(memory_info)
    pprint(interface_data)

    merged_dict = {**system_info, **cpu_info, **memory_info, **interface_data, ** network_stats}
    return jsonify(merged_dict)

    #return jsonify(**{
    #   "System Information": system_info,
    #   "CPU Information": cpu_info,
    #   "Memory Information": memory_info,
    #})


@app.route('/raft-peers', methods=['GET'])
def get_raft_peers():
    try:
        response = requests.get(f'{CONSUL_API_URL}/v1/operator/raft/configuration')
        data = response.json()
        pprint(data)
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)})

@app.route('/consul-info', methods=['GET'])
def get_consul_info():
    try:
        # Get the list of nodes registered with Consul
        nodes_response = requests.get(f'{CONSUL_API_URL}/v1/catalog/nodes')
        nodes_count = len(nodes_response.json())

        # Get the list of services registered with Consul
        services_response = requests.get(f'{CONSUL_API_URL}/v1/catalog/services')
        services_count = len(services_response.json())

        # Get the Consul cluster leader information
        leader_response = requests.get(f'{CONSUL_API_URL}/v1/status/leader')
        cluster_leader = leader_response.text.strip()
        pprint(cluster_leader)
        # Get the internal protocol version used by Consul
        version_response = requests.get(f'{CONSUL_API_URL}/v1/agent/self')
        consul_version = version_response.json()['Config']['Version']
        pprint(consul_version)

        # Get the internal protocol version used by Consul
        members_response = requests.get(f'{CONSUL_API_URL}/v1/agent/members')
        consul_members_list = members_response.json()
        pprint(members_response)
        # Prepare the structured tabular JSON response
        response_data = {
            'Number of Registered Nodes': nodes_count,
            'Number of Registered Services': services_count,
            'Cluster Leader': cluster_leader,
            'Internal Protocol Version': consul_version,
            "Registered Nodes": consul_members_list,
        }
        data = [ 
                {'Number of Registered Nodes': nodes_count},
                {'Number of Registered Services': services_count},
                {'Cluster Leader': cluster_leader},
                {'Internal Protocol Version': consul_version},
                {'Registered Members': consul_members_list},
            ] 
        pprint(data)
     # Convert JSON to HTML table
        table = jsonify_to_html(data) 
        return render_template("index.html", table=table)
        #return jsonify(data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/status', methods=['GET'])
def check_consul_server_status():
    try:
        # Define the URL of the Consul server you want to check
        response = requests.get(f'{CONSUL_API_URL}/v1/status/leader')
        data = response.json()
        if response.status_code == 200:
            pprint(data)
            message = ({"status": "1", "message": "Consul server is running"})
            pprint(message)
            return jsonify({"status": "1", "message": "Consul server is running"})
        else:
            return jsonify({"status": "0", "message": "Consul server is not running"})
    except requests.exceptions.RequestException as e:
        return jsonify({"status": "0", "message": f"Error: {str(e)}"})


@app.route('/services', methods=['GET'])
def get_services():
    try:
        # Define the URL of the Consul server you want to check
        response = requests.get(f'{CONSUL_API_URL}/v1/catalog/services')
        data = response.json()
        pprint(data)
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)})

def jsonify_to_html(data):
    # Create an HTML table from JSON data
    table = "<table>"
    for item in data:
        table += "<tr>"
        for key, value in item.items():
            table += f"<td>{key}</td><td>{value}</td>"
        table += "</tr>"
    table += "</table>"
    return table

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
