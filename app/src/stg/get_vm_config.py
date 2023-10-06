from flask import Flask, jsonify
import platform
app = Flask(__name__)

@app.route('/vm_config', methods=['GET'])
def get_vm_config():
    try:
        vm_config = platform.uname()
        return jsonify(vm_config)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    # Add code to query Vagrant VM configuration here
    # You can use subprocess to run Vagrant commands

    # Sample response data (replace with your Vagrant query logic)
    vm_config = {
        "vCPUs": 2,
        "memory": "4GB",
        "operating_system": "Ubuntu 20.04"
    }

    return jsonify(vm_config)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

