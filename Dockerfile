#FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
#FROM alpine:3.10
FROM  alpine:3.10.squashed
#FROM tiangolo/uwsgi-nginx-flask:python3.11
COPY ./app  /app
WORKDIR /app/src

RUN pip install requests
RUN pip3 install psutil
#RUN pip3 install docker
CMD python3 /app/src/apirun.py
