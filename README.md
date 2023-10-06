## Consul-API Exercise completed September 2023

Exercise includes two main parts: 

1. Building a Consul server and exposing Consul API 
2. Building an API service that exposes some endpoints

Write a small API service that will expose the following routes: 
	
	GET  /v1/api/consulCluster/status	
	GET  /v1/api/consulCluster/summary
 	GET  /v1/api/consulCluster/members
  	GET  /v1/api/consulCluster/systemInfo
   
## Vagrant VM Setup .\Vagrantfile ##<br />
Vagrant.configure("2") do |config|<br />
  config.vm.hostname = "consul-webdev-vm-1"  <br />
  config.vm.box = "shaunkrok/conlab_box"  <br />
  config.vm.box_version = "1.0.0.0"  <br />
  config.vm.network "public_network", ip: "10.100.102.100"  <br />
end<br />

config.vm.box = "shaunkrok/conlab_box"<br />
config.vm.network "public_network", ip: "YOUR-IP-ADDRESS on the host machine"<br />

## Create VM - Create directory on the host machine and execute the vagrant CLI commands:<br />
Base box image is a custom image stored on Vagrant cloud(public access)<br />
a. vagrant box add shaunkrok/conlab_box /path/to/vagrant-box.box <br />
b. vagrant init shaunkrok/conlab_box [ save or edit the existing .\Vagrantfile.example and update the config.vm.box]<br />
c. vagrant up<br />

## API Service ##

http://10.100.102.100:8080/status<br />
{"message":"Consul server is running","status":"1"}<br />

"message":"Error: HTTPConnectionPool(host='host.docker.internal', port=8500): Max retries exceeded with url: /v1/status/leader (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7ffb154e1710>: Failed to establish a new connection: [Errno 111] Connection refused'))","status":"0"} 


http://10.100.102.100:8080/consul-info <br />
JSON Data as HTML Table <br />

Number of Registered Nodes	1<br />
Number of Registered Services	2<br />
Cluster Leader	"127.0.0.1:8300"<br />
Internal Protocol Version	1.12.3<br />

Registered Members	[{'Name': 'consul-webdev-vm-1', 'Addr': '127.0.0.1', 'Port': 8301, 'Tags': {'acls': '0', 'bootstrap': '1', 'build': '1.12.3:2308c75e', 'dc': 'ob-lab', 'ft_fs': '1', 'ft_si': '1', 'id': 'e1292f96-3753-3bc8-2c7f-d52d485cb901', 'port': '8300', 'raft_vsn': '3', 'role': 'consul', 'segment': '', 'vsn': '2', 'vsn_max': '3', 'vsn_min': '2', 'wan_join_port': '8302'}, 'Status': 1, 'ProtocolMin': 1, 'ProtocolMax': 5, 'ProtocolCur': 2, 'DelegateMin': 2, 'DelegateMax': 5, 'DelegateCur': 4}] 


http://10.100.102.100:8080/services <br />
{"consul":[],"ping check if API container is responding to ping":[]} 

http://10.100.102.100:8080/raft-peers <br />

http://10.100.102.100:8080/systeminfo 
{"Available Memory (GB)":0.46,"CPU Cores":2,"CPU Usage":[1.0,0.0],"Disk utilization":[41555521536,9173929984,32364814336,22.1],"Logical CPUs":2,"Machine Architecture":"x86_64","OS Version":"#202207102230 SMP PREEMPT_DYNAMIC Sun Jul 10 22:34:05 UTC 2022","Operating System":"Linux","Processor":"","Total Memory (GB)":0.95,"eth0":{"duplex":2,"is_up":true,"mtu":1500,"speed":10000},"lo":{"duplex":0,"is_up":true,"mtu":65536,"speed":0}} 


Consul User Interface(UI)<br />
http://YOUR-IP-ADDRESS:8500/ui<br />
http://10.100.102.100:8500/ui<br />


