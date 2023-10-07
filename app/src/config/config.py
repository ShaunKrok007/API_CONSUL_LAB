import logging
from datetime import datetime

import syslog
import sys

CONSUL_API_URL = 'http://host.docker.internal:8500'  # Replace with your Consul server address
#CONSUL_API_URL = 'http://127.0.0.1:8500'  # Replace with your Consul server address

# Configure the logging to stdout
logging.basicConfig(
    level=logging.INFO,  # Set the logging level as needed
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler()]
)

# Open a connection to the syslog daemon
syslog.openlog("sysinfohost", syslog.LOG_PID | syslog.LOG_CONS)

def log_to_syslog(message):
    syslog.syslog(syslog.LOG_INFO, message)
    sys.stdout = sys.stderr = open('/var/log/syslog', 'a')
    syslog.closelog()
