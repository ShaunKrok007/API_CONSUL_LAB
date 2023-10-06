#!/usr/bin/python3
import os
import datetime
import requests
import json
from docker import Client

cli = Client(base_url='unix://var/run/docker.sock')
containers = cli.containers()

# Create a list to store container information as dictionaries
container_info_list = []

for container in range(len(containers)):
    container_info = {}
    for key in containers[container]:
        container_info[key] = containers[container][key]
    container_info_list.append(container_info)

# Define the path to the JSON file where you want to store the data
json_file_path = 'container_info.json'

# Write the container information list to a JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(container_info_list, json_file, indent=4)
    json_data = json.dumps(container_info_list, indent=4)
    print(json_data, flush=True)

print(f"Container information has been saved to {json_file_path}")
