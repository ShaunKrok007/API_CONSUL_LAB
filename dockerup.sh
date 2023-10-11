#docker run -e TZ=Asia/Jerusalem --log-driver "syslog" --add-host host.docker.internal:host-gateway -d -p 8080:5000 alpine:3.10 
#!/bin/bash
docker build -t python:3.8-slim .
docker run -e TZ=Asia/Jerusalem --log-driver "syslog" --add-host host.docker.internal:host-gateway -d -p 8080:5000 python:3.8-slim
docker container prune -f
cd /opt/flaskweb/app/src
/opt/flaskweb/app/src/getsyslog.py /dev/null &
/opt/flaskweb/app/src/sysinfohost.py /dev/null &
