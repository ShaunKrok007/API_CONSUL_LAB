## Consul-API Exercise completed September 2023


## Changes: ##
1. Added logging modules(deleted all print statments)
2. Added Flask Blueprints
3. Added config.config.py - managed variables and logging
4. Updated container to use Alpine image
5. Updated configuration to allow access to syslog via Flask
   https://10.100.102.100:5001/getsyslog <br />
6. Updated configuration for PSUTIL to access host instead of container
   https://10.100.102.100:5002/sysinfo <br />
7. Added new self-signed certificate for API  <br />

Exercise includes two main parts: 

1. Building a Consul server and exposing Consul API 
2. Building an API service that exposes some endpoints

Write a small API service that will expose the following routes: 
	
	GET  /v1/api/consulCluster/status	
	GET  /v1/api/consulCluster/summary
 	GET  /v1/api/consulCluster/members
  	GET  /v1/api/consulCluster/systemInfo
   
## Vagrant VM Setup .\Vagrantfile <br />
1. create a directory <br />
2. copy Vagrantfile to directory <br />
3. cd to directory <br />
4. vagrant up <br />
config.vm.network "public_network", ip: "YOUR-IP-ADDRESS on the host machine"<br />

## Create VM - Create directory on the host machine and execute the vagrant CLI commands:<br />
Base box image is a custom image stored on Vagrant cloud(public access)<br />
a. vagrant box add shaunkrok/conlab_box /path/to/vagrant-box.box <br />
b. vagrant init shaunkrok/conlab_box [ save or edit the existing .\Vagrantfile.example and update the config.vm.box]<br />
c. vagrant up<br />

## API Service ##

https://10.100.102.100:8080/status<br />
https://10.100.102.100:8080/consulinfo <br />
https://10.100.102.100:8080/services <br />
https://10.100.102.100:8080/raftpeers <br />
https://10.100.102.100:8080/sysinfo <br />
https://10.100.102.100:8080/healthcheck <br />

Consul User Interface(UI)<br />
http://YOUR-IP-ADDRESS:8500/ui<br />
http://10.100.102.100:8500/ui<br />
