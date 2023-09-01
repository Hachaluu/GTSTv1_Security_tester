# Scanning and Enumeration 

- Scanning is the second phase of hacking.
- refers to the package of techniques or procedures used to identify host port and various services within a system
## Why do we do Scanning 
- to identify HOST'S System detail
        - Operation System
        - Service version
- to discover open port
- to discover live systems
### Network Scanning
Is a method of scanning a network and getting more info.
for network: Nmap
for Subdomain: Sublister, subfinder
for website  vulnerability, Nessus, Acunitix
### Nmap - Network Mapper

Nmap is a network scanning and exploiting tool.
it scan network , port, os
made for windows and linux
to check the version 
```shell
nmap --version

```
 #### Live system discovery
it means checking up and running host(client/ server) on network

#### Ping Sweep
- a method of checking if the host is up or down
- it uses [ ICMP(Internet Control Message Protocol) ]package for checking purpose
- it sends [Echo request] and waits for if there is [Echo reply] then the system is up
- PING TAKES 1 HOST ONLY
### Nmap ping Sweep
Nmap can see the hole range
the syntaxes are 
```shell
nmap -sn IP
nmap -sn GatewayIP-255
nmap -sn GatewayIP/networks-CIDR notation 
(it does not work on virtual machines )
nmap -PnIP  (to jump host discovery)
```
# What is PORT
- Port is process-specific or an [application-specific software ]construct serving as a  communication endpoint, which is used by the Transport Layer protocols of Internet Protocol suite, such as[ User Diagram Protocol (UDP)] and [Transmission Control Protocol (TCP)]
- simply it is a door for a service/purpose 
- there are 65536 ports on a computer
	- 1-1024  = reserved (well known)
	-Example:
			- HTTP(80)- unsecured web port
			- HTTP(443)- secured web port
			- FTP(21)- File transferring port
			- SSH(22)- Secured shell port

## Port Status
- Open Port 
	- They are open for accepting any requests.
- Closed Port
	- They are not for accepting any request but there is some service running on it.

### Open port discovery
- For shell activity port 22 is open.
- But in some cases there are some open port without any intention.
- We can use Nmap to check a port
```shell
nmap IP   (only the 1000 port)
nmap -p port1, port2,port3 IP   (only port 123)
nmap -p IP (all the 65000 port)
```
# Scanning methods
- Nmap scans network in different modes
	- TCP connect (TCP scan)
	- TCP SYN (stealth scan)
	- UDP scan
	- Xmas scan
## TCP Scan
- TCP is the best on making connection.
- It use 3-way HANDSHAKE.
### 3-Way handshake
- Here When we start connection we will send a Synchronization flag.
- When the server got and accepted our request it will reply with 
Synchronization and Acknowledgment.
- Finally, we will send Acknowledgement or Reset(RST) and continue because we have connection/network now.
```shell
nmap -sT IP
```
## Stealth Scan
- Same as TCP but here we don't send the last ACK flag
- But we send the reset flag
```shell
sudo nmap -sS IP
```
## UDP SCAN 
- This is a method to scan if any service/ port is using UDP
- Is a slow process
```shell
sudo namap -sU IP
```
## Xmas Scan
- In this scan the first thing is to send FIN/PSH/URG instead of SYN
- If the response is like RST flag then the system is closed.
- If there is no response the system is open
```shell
sudo nmap -sX IP
```
# Operating system Detection 
```shell
sudo nmap -O IP   (os detection)
sudo nmap -A IP    (os with the version detection)
```
# Scan speed
- Nmap have a time waiting after sending 1 packages to a host.
- The nmap time template is -T (0-5)
	- Insane -T5
	- Aggressive -T4
	- Normal -T3
	- Polite -T2
	- Sneaky -T1
## Nmap Insane
- It only waits 0.3 seconds for the response, and also if nmap couldn't finish the scan in 15 minutes sit will give up on the host.
- Sometimes the accuracy is too low.
```shell
nmap -T5 IP
```
## Nmap Aggressive 
- It only waits for 1.25 second for the response.
- Nmap recommends using this for reasonable modern and reliable networks.
```shell
nmap -T4 IP
```
## Nmap Normal
- It is default nmap timi.
```shell 
nmap -T3 IP
```
## Nmap Polite and Sneaky
- The slowest timing of nmap.
- It helps to not be detected.
```shell
nmap -T2 IP
nmap -T1 IP
```
# Nmap Script Engine (NSE)
- Nmap can run a script on ports which are written in Lua-programming language.
- The scripts are located in /usr/share/nmap/scripts
- It contain a total number of 589 scripts
- You can write your own script if you can do Lua
```shell
nmap -sC IP
nmap --script scriptname.nse IP
```

[[S2Day3Malware.md]]
