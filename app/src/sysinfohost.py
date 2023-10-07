#!/usr/bin/python3 -u
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import platform
import psutil
import json
from flask import Flask, jsonify
import requests
from icecream import ic
from config.config import *
import time

app = Flask(__name__)

@app.route('/sysinfo')
def get_system_info():
    try:
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
        merged_dict = {**system_info, **cpu_info, **memory_info, **interface_data, ** network_stats}
        json_data = json.dumps(merged_dict, indent=4)
        logging.info(json_data)
        log_to_syslog(json_data)
        response = app.response_class(
            response=json_data,
            status=200,
            mimetype='application/json'
        )
        return response
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
