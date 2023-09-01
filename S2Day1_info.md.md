# Recon/Information Gathering/Footprint
- Information gathering is collecting data about network/host/system
- Footprint  =  Footstep + printing(logging)
## Need of recon
- To get access on system
- To know the system 
## Types of Recon
- Based on how we do the recon
	- Active foot printing  :> is when we try to gather the info directly from the person.
		-It is illegal without permission.
	- Passive foot printing :> is when we gather the info from another person 
## What type of information we gather
 - We gather info for different things:
1. Host
- Website
- Computer
- Smart Phone
2. Network
- Home network 
- Company network
3. person/organization
4. Application
### A. Website
- The info that we gather about a website are:
	- IP addresses
	- Development frameworks
		- Web server version
		- Technologies used
	- Name
	- Domain registrations
  ##### To get IP
  - Active recon
	  - ping  (website link)
	  - nslookup (website link)
  - Passive recon
	  - www.nslookup.io
##### To get Development framework
- Use this simple browser extension:
	- Wapplyzer
	- Builwith
- Terminal tool
	- whatweb
##### To know about domains
Website tool 
	whois
Terminal
	whois 
		sudo apt install whois
		whois
### B. Computers/Phones
- The info we gather are:
	- IP addresses
	- OS info
	- Host name
	- MAC address
	- Open services or ports
### C. Networks
- The info's are :
	- IP addresses
	- Ports, Services
	- Class and type of network
	- Host on the network
	- Strength and security of that network
### D. Personal Information
- The info's are :
	- Full name
	- Address
		- physical
		- social media address
		- phone address
	- what the person loves 
	- Job 
	- Friends
	- Status
	- Skills .............


- [+] To get names from phone number we can use 
	- [ ] True caller
- [+] Social media address 
	- [ ] If we have the persons full name we can search it on any browser
 #### IP  geolocation
 - If we get the IP address of the person we can insert it to 
	 - https://www.iplocation.net
### E. Applications/Soft wares
- The info we gather are:
	- In what language it is made of
	- Source codes
	- Their logic and Function
# Reverse image search
- It is a technique of searching with image 
- We can use:
● https://tineye.com/
● https://www.labnol.org/reverse/
● https://images.google.com/
# Google Dorking (Google Hacking Database)
- Involves using Google to identify vulnerabilities in website.
## Basic operators
- For inclusion of something common (+)
	- Hacking + python
- To exclude some terms (-)
	- Programing - python
- To search the exact value ("")
	- "How to become hacker"
- When we forgot some part of our prompt (* )
	- in this case google will think the (* ) to fill it automatically 
- To search two thing with or function ( | )
	- "hacking" | "HACKING"
## Syntaxes used by google
- [+] intitle
	- intitle: hack
- [+] inurl:
	- inurl: hacked
- [+] filetype
	- "hacking" filetype:pdf
- [+] Intext
	- intext : "hackers in ethiopia"

[[S2Day2_Scan.md]]
