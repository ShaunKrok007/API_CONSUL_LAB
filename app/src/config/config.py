import logging
CONSUL_API_URL = 'http://host.docker.internal:8500'  # Replace with your Consul server address
#CONSUL_API_URL = 'http://127.0.0.1:8500'  # Replace with your Consul server address

# Configure the logging
logging.basicConfig(
    level=logging.INFO,  # Set the logging level as needed
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler()]
)
