#!/bin/bash

# Decode the base64-encoded token
encoded_token="Z2hwX3dBWktZbWpoYU9OcnY1ZW9YTndETHhPbWlGM0hyQTM2SHhmMQ=="
token=$(echo $encoded_token | base64 -d)

# Clone the GitHub repository using the decoded token
git clone https://$token@github.com/ShaunKrok007/API_CONSUL_LAB.git /home/vagrant/test
