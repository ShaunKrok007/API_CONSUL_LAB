from flask import Flask, jsonify, render_template
import requests
import logging

logging.basicConfig(filename='apilog.log', level=logging.DEBUG)
app = Flask(__name__)

@app.route('/')
def main():
  # showing different logging levels
  app.logger.debug("debug log info")
  app.logger.info("Info log information")
  app.logger.warning("Warning log info")
  app.logger.error("Error log info")
  app.logger.critical("Critical log info")
  return "testing logging levels."

@app.route('/raft-peers')
def get_services():
    consul_url = 'http://host.docker.internal:8500/v1/operator/raft/configuration'
    
    try:
        response = requests.get(consul_url)
        response.raise_for_status()
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
