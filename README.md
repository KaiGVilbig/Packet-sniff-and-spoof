# Packet-sniff-and-spoof
Sniff and spoof using scapy

This is a project that runs with 3 docker container within seedlabs VM. 
It consists of 3 machines, A, B, and M. A and B want to communicate with eachother and M is a malicious attacker that will do a Man-in-the-Middle attack

Machine A: IP = 10.9.0.5, MAC = 02:42:0a:09:00:05
Machine B: IP = 10.9.0.6, MAC = 02:42:0a:09:00:06
Machine M: IP = 10.9.0.105, MAC = 02:42:0a:09:00:69

The lab containers and virtual network are created using Docker Compose, a tool for defining multi-container Docker applications. The configuration is specifed in a YAML file,docker-compose.yml.

To build and start the lab containers, you will use thedocker-compose buildanddocker-composeupcommands.

At this point, in order to interact with the containers, you will need to open another terminal windowto the VM.
Top stop the containers, run the command: docker-compose down

$ docker-compose up     # Start the container$ 
docker-compose down   # Shut down the container

// Aliases for the Compose commands above
$ dcbuild       # Alias for: docker-compose build
$ dcup          # Alias for: docker-compose up
$ dcdown        # Alias for: docker-compose down

To open a shell on one of the virtualized host containers, you will first need to find the container IDusing the"docker ps"command. Then a shell may be opened using"docker exec". Useful aliasesfor these commands are provided:
$ dockps        # Alias for: docker ps --format "{{.ID}}  {{.Names}}"
$ docksh <id>   # Alias for: docker exec -it <id> /bin/bash

poison.py is a program that runs on Machine M's computer. It poisons the cache of machines A and B so that the MAC address is M's MAC
therefor routing any packets through M instead of direct comm between A and B

sns.py listens on ethernet for packets with destination of machine M's mac address and changes all data to "Z"
snsNC.py does the same except it captures the datas, decopdes it and replace every instance of 'kai' to 'AAA'. 
