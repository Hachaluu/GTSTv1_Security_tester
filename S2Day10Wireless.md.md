# What is Wireless Network
- It is a set of two or more devices connected with each other via radio waves within a limited space range. 
- A [wire less router] is the most important device in a wireless network that connects the users with the internet.
## What is wireless hacking 
- It is cracking the security protocols in a wireless network.
- In a wireless network, we have Access Points(AP), A wireless access point (wireless AP) is a network device that transmits and receives data over a wireless local area network (WLAN):
	- serve as the interconnection point between the WLAN and a fixed wire network
	- Found inside the wireless router
- When our wireless cards are converted in sniffing modes, they are called [monitor mode.]
- When your wireless card allows to configure a AP on your laptop manually it is called Managed mode.
## WIFI Hacking
- We need wi-fi antenna for our computer but the adapter have to have a feature called "*Packet Injection + Monitor Mode*". 
## Wireless network Algorithms
- Terms
	- SSID/Service set identifier/: it is the name of the AP
	- BSSID/ Basic Service Set Identifier/: Mac address of the wireless AP device
	- WLAN: Wireless local area network same as wi-fi
	- Channel : are smaller bands with in wi-fi frequency bands that are used by your wireless network
		- 13 wi-fi channels are in the 2.4 GHz frequency band 
		- 45 WI-FI channels are in the 5 GHz frequency band
	- There are Four types of WLAN security Algorithms
		- WEP
		- WPA
		- WPA2
		- WPA3
### WEP - Wired Equivalent Privacy
- It encrypts traffic using a 64 or 128 bit key in hexadecimal and this a *static key* which means every traffic in the device is encrypted using a single key.	
- *WEP Key* allows a computer on a  network to exchange encoded messages while hiding the message's contents from intruders and it is used to connect to a wireless security enabled network, it's main goals was to prevent Man-in-the-Middle attacks.
### WPA - Wi-Fi Protected Access
- It was a wi-fi alliance's replacement for WEP.
- *Temporal key integrity Protocol* this dynamically changes the key that system use.
- The key used in WPA is 256 bit
- WPA key is the password from whoever runs the network. 
### WPA2 - Wi-Fi Protected Access 2
- It operates in two modes:
	- *Personal or Pre-shared key (WPA2-PSK)* - It relied on a shared passcode for access and is usually used in home environments.
	- *Enterprise mode(WPA2-EAP)* - It is more for organizations .
- Both modes use the CCMP (Counter Mode Cipher Block Chaining Message Authentication Code Protocol)- It is based on advanced Encryption Standard (AES) which provides message authenticity and integrity verification 
- WPA2 is vulnerable to key reinstallation attacks (KRACK) this will exploit a weakness in WPA2 which allows attackers to pose as a clone network and force the users to login to the fake  malicious network.
### WPA3 - Wi-Fi protected Access 3
- It introduced 
	- *Individual data encryption*: When logging on to a public network, WPA3 signs up a new device through a process other than a shared password. 
		- WPA3 uses a Wi-Fi Device Provisioning Protocol (DPP) system that allows users to use near field communication (CFC) tags or QR codes to allow devices on the network.
		- It uses GCMP-256 encryption .
	- *Simultaneous Authentication of Equals Protocol*:
		- It is used to create a secured handshake 
		- If the users password is weak it uses more secure handshake using Wi-Fi DDP.
## WLAN RECON
- To check our adapters mode:
```shell
iwconfig
#to change it we use a tool called "airodumdp-ng"
sudo airodump-ng start (interface)
```
- on a wireless network we gather :
	- SSID/ESSID
	- BSSID
	- Channel
	- Algorithm
	- Manufacturer of the Router
to get info our wi-fi
```shell
sudo airodump-ng (interface) 
```
![[Pasted image 20230829095314.png]]
## Hacking WLAN
- Some Hacking methods for wi-fi networks.
	- WPS enabled
	- Handshake Brute force
	- WEP Attack
	- Evil-twin attack
### 1. WPS enabled
- Wi-Fi Protected Setup (WPS) is a feature supplied with many routers. 
- It is designed to make the process of connecting to a secure wireless network from a computer or other device easier.
- WPS uses some 8 digit code to connect. And attacker will brute force this pin.
- ![[Pasted image 20230829095751.png]]
- [ ] Prevention 
-  We need to disable it from the router setting 
### 2. Handshake Bruteforce

- is the exchange of information between the access point and the client at the time the client connects to it.
- It is 4 way handshake.
- Hackers will try to kick a person from a wi-fi(called deauthentication) and sniff the network, when the user try to connect back, they will have the Handshake file and the file can be bruteforced and got the right password.
- To do this:
	1. Get wifi info
	2. Sniff on that wi-fi specific channel
	3. Deauthenticate the wifi(on different shell)
	4. Get the handshake
	5. Crack it with aircrack.
![[Pasted image 20230829100744.png]]

#### Sniffing to the network
- We listen to specific channel of the target.
	- example: channel 4
```shell
airodump-ng (interface) -channel (channel) -w (filename)
```
![[Pasted image 20230829100953.png]]

- [ ]  DEAUTH
- On another terminal we do deauthentication attack.
- Syntax:
```shell
airplay-ng -0 (size) -a (Mac_of_target) (interface)
#-0 means how many times deauth is sent
#-a is the attack target
```
![[Pasted image 20230829101418.png]]
- [ ] Capturing Handshake
![[Pasted image 20230829101548.png]]
- After we got the handshake we need to crack it and get the password, to do this we use a tool called "Aircrack-ng"
```shell
sudo apt install aircrack-ng
```
- [ ] We need worklist
- Example for worklist is rockyou.txt
![[Pasted image 20230829101834.png]]

- [ ] Cracking 
- syntax
```shell
aircrack-ng (cap_file) -w (wordlist)
```
- [ ] Prevention way
1. Using WPA3 which is a newer protocol is your best bet 
against such an attack.
2. To mitigate against de-authentication attacks
3. use an ethernet connection if possible.
4. use a strong passphrase (not a password) to minimize the attackers chances of getting it
	a. Example: my home wifi password is something like: 
	“Helloworldthisismypassword”
	b. This will be very hard to crack it wordlist.
## 3. WEP attack 
- Same step with Handshake but here we will bruteforce an encryption key and also we don't capture handshake we only listen for WEP wi-fi for some minute, and we will crack it with aircrack-ng. 
![[Pasted image 20230831125747.png]]![[Pasted image 20230831125732.png]]
![[Pasted image 20230831125801.png]]
![[Pasted image 20230831125820.png]]
![[Pasted image 20230831125830.png]]
- [ ] Prevention 
	- [ ] Don't use it
## 4. Evil-twin Attack
- Includes 
	- Deauthentication
	- Fake AP and 
	- phishing.
- [ ] The way it work is:
	- Attacker will clone one of the wifi he going to attack with making it open wifi
	- Then it will initiate deauth on real wifi, so users will be forced to be on the fake one.
	- Then the attacker will fake prompt to input the password to access the wifi
	- When the users add the password,  Attacker will have the password.
 - To do this it will require a lot of complicated things, but there are tools that can do this automatically.
	 - Airgrddon  (https://github.com/v1s1t0r1sh3r3/airgeddon)
	 - To install it in kali
```shell
sudo apt install dnsmasq hostapd-wpe dhcp-server hostapd mdk4 hcxdumptool hcxtools beef-xss lighttpd xterm asleap
```
![[Pasted image 20230831130817.png]]
![[Pasted image 20230831130829.png]]
![[Pasted image 20230831130836.png]]
![[Pasted image 20230831130842.png]]
_____
- [ ] To do this attack we need two wi-fi adapter 
	- [ ] To create the phishing page and fake APs
	- [ ] To Deuth the users
Running 
![[Pasted image 20230831131149.png]]
![[Pasted image 20230831131156.png]]
![[Pasted image 20230831131210.png]]
![[Pasted image 20230831131221.png]]
And there are so many steps 

- [ ] Prevention
	● Avoid Wi-Fi networks marked as “Unsecure”
	● Use your own hotspot
	● Disable Wi-Fi autosave
	● Use a VPN
	● Only browse HTTPS sites
## Bluetooth Hacking 
- Bluetooth is a universal protocol for low power, near field communication operating at 2.4 - 2.485 GHz using spread spectrum.
- Any two devices that in the Bluetooth connection  we transfer the following data:
	- Name
	- Class
	- List of services
	- Technical Information

- [ ] To do Bluetooth pentest we need a bluetooth adapter . (Our computer has its own)
- [ ] Install :
```shell
sudo apt install bluetooth bluez bluez-tools rfkill blueman
```
![[Pasted image 20230831132934.png]]
config 
- We will unblock our bluetooth 
device
- We will start the bluetooth service
- To get information about your bluetooth device.
	- hciconfig 
	- ![[Pasted image 20230831133302.png]]
- To Scan the bluetooth nearby
	- hcitool scan
	- ![[Pasted image 20230831133330.png]]
![[Pasted image 20230831133209.png]]
## Bluetooth Attacks 
1. Bluetooth Jacking : Sending message over bluetooth
2. Bluetooth Smaching : it is DDOS for bluetooth
3. Bluebugging : The attacker is able to take control of the target's phone.
Bloover was developed as as POC tool for this pupose.
# SS7 Attack
- is a security exploit that takes advantage of a weakness in the design of SS7 (Signaling System 7) to enable data theft, eavesdropping, text interception and location tracking.
- For this purpose u need a device that can intercept a cellular signals
- Intercepting Device![[Pasted image 20230831134236.png]]
- [ ] RFID Attack
- [ ] Card cloning 

