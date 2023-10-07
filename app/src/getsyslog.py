#!/usr/bin/python3 -u
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

# blueprints/getsyslog.py
#!/usr/bin/python3 -u
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import json
from flask import Flask, jsonify
import requests
import subprocess

app = Flask(__name__)

@app.route('/getsyslog')
def get_syslog_tail():
    try:
        # Use subprocess to run the 'tail' command
        syslog_tail = subprocess.check_output(['tail', '-n50', '/var/log/syslog']).decode('utf-8')
        response = app.response_class(
            response=syslog_tail,
            status=200,
            mimetype='application/json'
        )

        return response
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
