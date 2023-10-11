FROM python:3.8-slim
COPY ./app  /app
WORKDIR /app/src
RUN pip install requests 
RUN pip install flask
RUN pip3 install psutil
CMD ["python3", "/app/src/apirun.py"]
