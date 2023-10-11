# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
# Vagrantfile
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.network "public_network", ip: "10.100.102.101"
  ###------------------------------   Provisioning   -------------------------------###
  config.vm.provision "Provisioning", type: "shell" do |s|
    s.inline = <<-SHELL
    # Enable password authentication in sshd_config
    sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
    # Restart SSH service to apply changes
    service ssh restart
    # Update and install required packages
    apt-get update
    apt-get install -y python3-pip unzip
    pip3 install flask
    pip3 install psutil
    pip3 install icecream
    # Install syslog-ng
    apt-get install -y syslog-ng

    # GITHUB Clone REPO
    mkdir -p /opt/flaskweb
    echo 'export GITHUB_TOKEN=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' >> /vagrant/.bashrc
    source /vagrant/.bashrc
    # Clone the repository with authentication token
    git clone https://$GITHUB_TOKEN@github.com/ShaunKrok007/API_CONSUL_LAB.git /opt/flaskweb -b main
    rm /vagrant/.bashrc
    sudo snap install gh
    # Install Consul
    apt-get install -y unzip
    wget https://releases.hashicorp.com/consul/1.16.2/consul_1.16.2_linux_amd64.zip
    unzip consul_1.16.2_linux_amd64.zip
    mv consul /usr/local/bin/
    rm consul_1.16.2_linux_amd64.zip
    # Create the /etc/consul.d directory
    mkdir -p /etc/consul.d
    # Create and configure the agent.hcl file
    echo '{
      "server": true,
      "bootstrap_expect": 1,
      "bind_addr": "127.0.0.1",
      "datacenter": "oblab1",
      "log_level": "INFO",
      "enable_syslog": true,
      "ui": true
    }' | sudo tee /etc/consul.d/agent.hcl
    # Start Consul
    sudo consul agent -server -bootstrap-expect 1 -bind=127.0.0.1 -data-dir=/tmp/consul -config-dir /etc/consul.d -ui -client=0.0.0.0 > /dev/null &
    # Install Docker
    sudo apt-get install -y docker.io
    sudo systemctl enable docker
    sudo systemctl start docker
    # Start API
    cd /opt/flaskweb/
    sudo ./dockerup.sh
  SHELL
  end 
  config.vm.provider "virtualbox" do |vb|
    vb.memory = 2048
    vb.cpus = 2
  end
end
