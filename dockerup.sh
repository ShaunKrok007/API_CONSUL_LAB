#!/bin/bash
#app_name="docker-flask-api"
app_name="alpine:3.10"
docker build -t ${app_name} .
#docker run -d -p 8080:5000 --add-host host.docker.internal:host-gateway -name=${app_name} -v $PWD:/app ${app_name} 
docker run --log-driver "syslog" --add-host host.docker.internal:host-gateway -d -p 8080:5000 alpine:3.10 
