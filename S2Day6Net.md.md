# Networking for Hacking 
- It is gathering and exploiting of networks.
- It is offensive branch of computer security. 
- It includes 
	- Network information gathering 
	- Sniffing
	- Network attacks
## Network Foot printing
- It means gathering info about the domain by using tools
	- Ping
	- traceroute
		- It is used to trace out the route taken by the certain information.
		```shell
		traceroute google.com
		```
## Network Sniffing
- It is the process of monitoring and capturing all the packets passing through a given network .
- Types of sniffing
	1. Passive Sniffing
		- In this kind of sniffing we can only be able to listen only 
		- It works with HUB devices. On a hub device, the traffic is sent to all the ports. In a network that uses hubs to connect systems, all hosts on the network can see the traffic.
	2. Active Sniffing 
		- In this sniffing the network may not only be listened but also it can be altered.
		- It is used to sniff a switch based server
# Wire Shark
- It is one popular passive monitoring tool.
- It uses only passive observation of the network traffic. 
```shell
wireshark
```
# Tshark
```shell
tshark -l (interface)
```
# ARP
what is ARP (Address Resolution Protocol)
- It is a procedure for mapping a dynamic IP address to a permanent physical machine address n a LAN.
- ARP is used for a computers to start a connection they need a mac address of  a destination .
# Mac Flooding
- It is a method of attacking a network switches .
- Mac table consists of individuals mac address of the host computer on the network on the network which are connected to port of the switch.
- The plan of the attack is to take down the MAC table.
- The attacker sends Ethernet Frames in a huge number. When sending many Ethernet Frames to the switch, these frames will have various sender addresses. 
- We can use macof tool for the mac flood
```shell
sudo macof -i (interface)

macof -i (interface) -n 10  -d (ip)
```
## Prevention
1. Port Security – Limits the no of MAC addresses connecting to a single port on the Switch.
2. MAC Filtering – Limits the no of MAC addresses to a certain extent
# ARP Spoof  (ARP poisoning)
- ARP translates IP into mac.
- It is a Man in the Middle (MitM) attack that allows the attacker to intercept communicate between network devices 
![[Pasted image 20230824212143.png]]
To do this 
1) We will get the mac of our gateway
2) We will get our linux machine mac
	- arp -g
3) Enable ip forward
	-  sudo sysctl net.ipv4.ip_forward=1
4. Start the spoofing with arpspoof tool
	-  Arpspoof -i interface -t target -r defaultgatewayip
 In advanced Method 
```shell
sudo apt install bettercap
sudo bettercap -face (interface)
# To scan the network
# after getting inside bettercap 
net.probe on
net.show
# To start arp spoofing 
set arp.spoof.target (ip)
arp.spoof on
# To start MitM
net.sniff on
net.sniff off
```
## Prevention 
1. Using static ARP tables: manually setted
2. Switch security: some feature for ARP poisoning
3. Encryption: not for arp but in case of leaks

[[S2Day7Anon.md]]
