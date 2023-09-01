# Anonymity and DOS
# Anonymity
- It is simply using fake profile, location, identity, personality
- It will your identity private but not your actions.
## Online Privacy
- A programs like incognito tabs are a program that won't save our history on their server but still they will have our ip address and other info will be known by our ISP(internet service provider) .
- So they don't give us real privacy.
## Methods of Anonymity
1. Proxy chains
2. Tor Network
3. VPN
4. Mac change
5. Incognito
6. Secured OS
7. Temp mail
8. Temp number
### What is Proxy Server
- Is a system or router that provides a gateway between users and the internet.
### Proxy Chains
- It is a chains of proxy.
### Types of Proxy chains
1. Dynamic chain
2. Strict chain
3. Round Robin Chain
4. Random Chain
#### Dynamic Chain
- In this way the proxy servers are chained as the list is given.
- If the is a server that is not working.
- If any of them are not working it will display error.
#### Strict Chain
- The proxies are chained as the list .
- If one is not working it will display error so every proxy must work.
#### Round Robin
- It will follow the proxy list.
- It will skip if 1 proxy is not working and if all is not working it will start again.
#### Random Chain
- It will random proxies and make a chain.
- If one is not working it will be skipped.

1. some proxy servers to use
[https://geonode.com]
2. Open /etc/proxychains4.conf
	- Turn on any kind pf proxy
	- put your proxy server
3. Accessing with proxychains
	1. Add “proxychains4” in front of any command.
	-  Find a working proxy server and you are good to go!
	- ![[Pasted image 20230824061055.png]]
	- ![[Pasted image 20230824061119.png]]
# T.O.R (The Routing Network)
- It enables anonymous web browsing.
-  The worldwide Tor computer network uses secure, encrypted protocols to ensure that users' online privacy is protected.
- It uses the onion-style routing technique for transmitting data.
### Torghost
- To install : clone it from github
	- https://github.com/SusmithKrishnan/torghost
	- install tor
![[Pasted image 20230824061827.png]]
```shell
git clone (link from github)
sudo aot install tor
sudo python3 torghost.py
sudo python3 torghost.py --start
sudo python3 torghost.py --stop
```
## VPN
- VPN means virtual Private Network
- It establishes a secure, encrypted connection.
## Mac Changer
- Mac can tell about our device so if we change our mac address we can change our id.
```shell
#to check if ther is macchenger
macchanger -l
#first we have to turn off our current mac
sudo ifconfig wlan0(interface) down
sudo macchanger -r wlan0(interface) # change the mac random  
sudo ifconfig wlan0(interface) up
macchanger -s (network interface wlan0 or )  # to check current mack status
sudo macchanger -n (mac address) (interface)

```
# Secure OS
- This are operating system that have a security and privacy features.
# Temporary Mail
- This will provide you a fake e mail address. 
- https://temp-mail.org/
# Deep web
- It refers to all the web pages that are not indexed by search engines and can not be accessed through traditional searches.
- Includes :
	- content that are protected by password, database,...... like:
		- private email account
		- online banking portals
		- subscription based on website
# DARK WEB
- It is not indexed by search engines.
- The dark web is a small portion of the deep web that is intentionally hidden and requires specific software or configurations to access.
- Their link ends with .onion because it uses Tor browser
## Starting
- There are specific os that are planned and made for dark web access
	- Tails OS
	- Whonix OS
	- Qube OS
- Tor is very slow and it may show you a wrong result according to your internet speed.
```shell
sudo apt install torbrowser-launcher
```
## Hidden Wiki
These are dark web links
# DOS AND DDOS Attacks
- DOS - Denial of Service attacks
- DDOS - Distributed Denial of Service Attack
- These are attacks that are made by sending too many requests to a server or a computer , this crashed the targeted website and makes it unavailable.
- DDOS attack is made when the requests came from different computers.
- It is highly illegal.
- Techniques:
	- SYN floods
		- sending lots of SYN
	- Service Request floods
		- Create many connections
	- Application level DOS
		- Exploiting vulnerability like
			- Buffer Overflow
			- SQL injection 
### Tools for DOS
1. SolarWinds Security Event Manager (SEM)
2. ManageEngine Log360
3. HULK
4. Tor’s Hammer
5. Slowloris
6. LOIC
7. Xoic
8. DDOSIM
9. RUDY
10. PyLoris
```shell
sudo python torshammer.py

```
### Prevention Ways
- Setting up fire walls
- Eliminate and patch known vulnerability
- Limit or shut off broadcast forwarding 
- DDOS  protection by cloud flare 

[[S2Day8Sys.md]]
