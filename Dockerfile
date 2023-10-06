#FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
FROM alpine:3.10
#FROM tiangolo/uwsgi-nginx-flask:python3.11
WORKDIR /src/app
COPY .  /src 

RUN pip install requests
RUN pip3 install tabulate
RUN pip3 install psutil
RUN pip3 install docker
CMD python3 /src/app/src/apirun.py
