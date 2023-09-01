cryptography
# What is Cryptography
- Science of a secret or hidden writing.
- It has two main components :
	- Encryption (hiding messages)
	- Authentication and Integrity 
## Encryption
## Cipher
- It is a method for encrypting messages
- The key which is an input to the algorithm is secret.
- KEY is a string of number or characters
- There are two kind:
	- [Symmetric] (when a same key is used for encryption and decryption)
	- [Asymmetric] (when different key is used for encryption and decryption)

### Symmetric Algorithm
Example:  Caesar Cipher
Types: 
	-  Block Cipher
		- Encrypt data one block at a  time (64 bits or 128 bits)
	- Stream Cipher
		- Encrypt data one bit or one byte at a time
		- Used if data is a constant stream of information.
### Substitution Ciphers
### Caesar Cipher
- It is a method in which each letter in the alphabet is rotated by three letters. 
### Using a key to shift alphabet 
- Obtain a key to for the algorithm and then shift the alphabets
	- For instance if the key is word we will shift all the letters by four and remove the letters w, o, r, & d from the encryption
[rot13.com]
### Asymmetric Encryption
- Uses a pair of keys for encryption:
	- public key
	- private key
- Messages that are encoded using public key can only be decoded by the private key. 
- The types are :
	- RSA
		- DEVELOPED BY Ron Rives, Adi Shamir, Len Adelman
		- public and private key are interchangeable
		- key size(512, 1024, 2048)
		- popular
		- has a maths formula to generate the keys
	- EL Gamal
		- Developed by Taher ElGamal
		- key size (512 or 1024)
# 3 Terms of Cryptography
1. Encoding / Decoding
- A method of creating a cipher text with out using any key
- Can be done by doing math on the given input / substituation 
2. Encrypting/Decrypting
a) This is method of creating Cipher text with keys.
b) To decrypts this kind u need to have the private key
- Example: DES,AES,RSA 
3. Hashing
a) This is a method of creating Cipher text with respect to a created hash
b) To reverse the hash, you just search for some match, you don't 
decrypt/decode it.
c) Salt: is a random string used for data modification for password protection.
- Example: MD5,sha254,...
## Kinds of encodings/encryptions
● Base2 01100010 01110010 01100101 01100001 01101011 01101001 
01110100
● Base8 142 162 145 141 153 151 164
● Base16 62 72 65 61 6b 69 74
● Base32 MJZGKYLLNF2A====
● Base58 4jP4KDubX1
● Base62 22udqyscMu
● Base64 YnJlYWtpdA==
● Base85 @WH$gCM@k
● Base91 %zmfv;:YH
● URL encode: hello%20there%20%3F
● Md5: 5d41402abc4b2a76b9719d911017c592
● Sha1: aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d
● Rot : Uryyb, Frphevgl Grfgref
# Tools
- [+] hashid
![[Pasted image 20230823151902.png]]
- [+] Cyber chef (web)
	- [ ] magic
	- [ ] base
	- [ ] form (to decrypt )
	- [ ] to (to encrypt)
## Decoding / Decrypting
There are so, many way to reverse some hashes/ciphers.
● Hashes
	- Craskstation.net(non-salted)
	- Own cracking(google the name)
● Encodings
	- Cyber Chef
- By searching the hash type and it self
# Python for Cryptography
- Example by XOR
```python 
def encrypt():
	msg=input("message")
	key=input("key: ")
	encrypt_hex = ""
	key_itr=0
	for i in range(len(msg)):
		deciText=ord(msg[i]) ^ ord(key[key_itr])
		key_itr+=1
		if key_itr>=len(key):
			key_itr=o
		encrypt_hex += hex(deciText)[2:]
	print(f"Message Encrypted Sucssfully!\nMessage: {encrypt_hex}")

def decrypt():
	msg=input("Message: ")
	key=inout("key: ")
	hex2uni = ""
	key_itr = 0 
	decryot_text = ""
	for i in range(0,len(msg),2):
		hex2uni+=bytes.fromhex(msg[i:i+2]).decode('ust-8')
	for i in range(len(hex2uni)):
		temp = ord(hex2uni[i]) ^ ord(key[key_itr])
		decrypt_text+=len(temp)
		key_itr+=1
		if key_itr >= len(key):
			key_itr = 0
	print(f"The Decrypted Message is:\n{decrypt_text}")


print("=======================")
print("Welcom to the Encrypter")
print("=======================")
user=input("what do you want to do\n 1) Encrypt \n 2) Decrypt \n>>")
if user == '1':
	encrypt()
elif user == '2':
	decrypt ()
else:
	print("Error, No input")
```
## Base64 decode / encode
```python
import base64
msg=input("text")
encode=base64.b64encode(bytes(msg,'utf-8'))
print(encoded)

decoded = base64.b64decode(encode)
print(decoded)

```

# Obfuscation
- Is the act of creating source or machine code that is difficult for humans or computer to understand.
- So in order not to let peoples and computers read our code we have to obfuscate it.
- Example:
	- The code is:
```
import base64
msg=input("text")
encode=base64.b64encode(bytes(msg,'utf-8'))
print(encoded)

decoded = base64.b64decode(encode)
print(decoded)
```
- The obfuscation version of the code is:
```
#pip install pycryptodome  , It works only v3.11 Above.
import random ,base64,codecs,zlib;pyobfuscate=""

obfuscate = dict(map(lambda map,dict:(map,dict),['(https://pyobfuscate.com)*(encrypt)'],['''8Qy|l9$oP0mG_3$l7b|FYRj2ieig%2z5ZyLXdl-dK6we%*`wtv**dr}lpA%ZFtjT9UCtcMVBO6wRYifI0-$p0<Swsp*8GF<8wr5b!K&uAkg}TC{A|8F>K<QJ`&od|R-2GxusAt=?QDPfg3<-|-`1OO-n|e(4vtow%Rtp|H9sQdzLlu;<-tj&X7YCoAOxY+_pD|'''.replace('\n','')]))

_=lambda OO00000OOO0000OOO,c_int=100000:(_OOOO00OO0O00O00OO:=''.join(chr(int(int(OO00000OOO0000OOO.split()[OO00O0OO00O0O0OO0])/random.randint(1,c_int)))for OO00O0OO00O0O0OO0 in range(len(OO00000OOO0000OOO.split()))));eval("".join(chr(i) for i in [101,120,101,99]))("\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x5f\x22\x2c\x70\x72\x69\x6e\x74\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x22\x2c\x65\x78\x65\x63\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x22\x2c\x65\x76\x61\x6c\x29");__='600840 10052792 2475510 107811 3460338 725070 743968 2892000 2595808 1123520 4498098 4658724 9505818 3510345 255392 146490 5557929 9774387 9643374 676195 8169140 8968656 7951905 2729216 6994785 2809039 2272480 238206 8998248 10083880 1132512 1887269 9978295 4040976 199290 720029 6381240 390456 4855272 5536608 8270336 5334956 137240 1950112 813888 1000864 14176 4719645 7434130 4414928 6253299 9947928 1058600 1230358 2126544 2411955 8232000 3136064 3545955 10065990 11478610 1845676 5793228 1659528 8606412 2662784 9252354 3826789 8515228 10136529 9876386 4503170 4636636 3050030 2304864 8648920 3476588 1063810 6624464 4304298 1150491 8042410 11245620 2352544 7278969 5070780 3834960 143016 6244008 3168128 11537244 1865133 1213344 1977057 519120 3126900 1538392 2683994 3910416 125890 1943840 169376 2568608 2306112 1493210 846355 4957785 3989836 8217104 10113987 6212658 6166328 5037850 7088140 89080 2665299 9719915 11920920 8955970 163995 576706 283176 3952332 6138720 8659980 10319940 3459800 1280676 161860 51870 2435250 6931656 3196522 1527030 341905 7265895 9809455 5280688 6588183 1684008 10751112 3620735 3711935 2101440 809948 7445910 7656305 6875824 7874685 7469960 4394725 5493528 3843530 1205130 2690707 1967374 2228611 1179175 1150372 171600 701454 4804904 669900 5363840 4755408 11124985 3124634 2961893 2837437 10306240 6771644 3092793 3541328 182988 7504380 2047000 2964060 3378704 8487488 7190998 3697158 1008513 9005208 7376139 3927743 9552368 2742597 5133926 6206652 2311680 3009798 833028 10506608 3530296 4332300 1356850 2624527 2751793 2669733 2394070 3060196 9653172 845520 3047668 1129650 1732414 1747310 6141852 3553786 8646840 10742180 287180 1469024 8047488 11999933 3563346 859220 420224 1719072 288032 236160 8018628 6755070 3157506 9098557 82624 8832714 3347765 2617768 861504 1658215 5273592 2594072 661024 902160 6018871 5059712 9333546 5543478 10761204 2640896 8903453 1575480 7633185 2561625 10578968 1218540 2351744 2321307 6116045 1633408 7015763 5559960 703580 194336 3119584 275968 733760 8284032 10978086 2905647 3348153 823648 7268835 6811105 2865536 6322155 8007685 196784 7085907 1614012 2185672 1955680 2770597 3622466 1278320 2700033 3743630 6963888 713088 5437432 1507305 2370048 8338983 4488036 4277988 9789636 9784072 5294239 4570980 2052020 2932737 873420 692064 2712832 1440256 493184 2269836 5935947 2087019 3347070 9042473 2466925 1163640 715299 5119400 61600 6803360 3070472 3586505 7106652 2033070 3448770 1332254 3203700 10746064 3431176 5216964 6666840 4895988 1158993 1447466 1891930 7078112 6234472 5222771 3231394 5588080 4378418 11000396 10886880 8793728 1153926 5624706 10051328 4147000 877546 3422952 2137083 9117108 160089 559164 5589552 1199496 4719258 5596015 6874390 2490348 1775612 1560720 4793584 715768 4420870 1858864 1768731 6089081 782892 9675759 443322 3954581 1434120 5588080 7513732 9453620 9258872 2909040 2799450 94254 10129700 9949920 11461032 497182 218660 779670 2491648 2679584 494368 352064 4780650 2815914 294496 7500159 7957680 3969000 180320 2806720 695360 4723901 2923730 6454392 9958698 3237507 9151509 4419136 548540 636352 2456512 1158016 760864 1530048 1579104 2585568 430784 2442792 6334013 8462433 5897208 1869828 4518740 3117160 5861968 1116906 2769468 816450 2827072 1415232 1191040 2284736 8500463 5873256 4862550 8653986 474048 4160392 11480880 2319080 5977776 4726700 1302857 2626355 2011353 6087816 4281612 7839 8072324 1344846 941040 376416 1535392 25216 1638144 940672 908128 1618464 2692032 10648056 9403706 9440490 4338990 8526326 10022230 3095680 5052656 1556850 3580776 899200 322624 1953120 70272 295072 4593225 1466046 1091200 6202410 2524200 3669480 7108528 2021742 3980813 775188 2749880 879060 7325537 2466936 3110290 5079795 2893968 18560 2327936 929024 2551104 2492384 250208 2255232 2757472 1236384 1442994 8935815 6523840 4058288 758816 5608275 159264 4936678 7766440 635360 3872280 3241388 98154 46120 2160368 1370625 2638555 1671604 1677458 10174381 1842902 2885703 1477056 2982847 11056675 3048096 4126658 5386576 8473294 255852 9015797 5719266 523215 5380544 7602876 3131200 3952665 5033820 6584982 3005160 3080910 7898256 1513884 2341428 858130 2530240 1594784 2112896 2613536 9160801 10402320 9666407 2264229 3761800 3583302 3224816 6873656 7062880 2358440 1934464 2074850 443128 2641596 11325900 7407946 5716016 5132800 3202520 2705549 2412399 473240 41376 1962080 2383136 2582624 116230 8708018 5645880 6635178 8949913 7043904 9106580 3237618 801350 193792 558464 1907744 2121536 7285534 6910080 4454403 7914654 3865800 9856668 3906900 1701828 590760 464890';why,are,you,reading,this,thing,huh="\x5f\x5f\x5f\x5f","\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f","\x28\x22\x22\x2e\x6a\x6f","\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c","\x31\x30\x31\x2c\x39\x39","\x5f\x5f\x29\x29","\x5d\x29\x29\x28\x5f\x28";b='eJxzdK8wccz1A+IwYyBt6OheketYHmYKAFuyB3k=';____("".join (chr (int (OO00O0OO00O0O0OO00 /2 ))for OO00O0OO00O0O0OO00 in [202 ,240 ,202 ,198 ] if _____!=______))(f'\x5f\x5f\x5f\x5f\x28\x22\x22\x2e\x6a\x6f\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c\x31\x30\x31\x2c\x39\x39\x5d\x29\x29({____(base64.b64decode(codecs.decode(zlib.decompress(base64.b64decode(b"eJw9kN1ygjAUhF8JIkzlMo6mEnIcHVIM3AGtoPIT2wSSPH2p7fTu252d2T3n3MkyK896dLvrSMIeaGxEGn0l/rpiLu3hlXm5yxDmO8tQZIDoeUQLr4oWePxk8VZfBpr9af8mXdzLTk8swRbP25bNzPvP8qwWJDRA8RX4vhLkfvuk0QRl3DOUekDC9xHZVnBcyUnXY7mtBrIOBDEKXNRl3KiBBor25l5MN7U5qSA/HsJiVpfsVIQ/Hj4dgoSYOndx+7tZLZ2m3qA4AFpUD6RDsbLXB2m0dPuPZa8GblvoGm/gthdI+8PxyYtnXqRLl9uiJi+xBbqtCmKm8/K3b7hsbmQ=")).decode(),"".join(chr(int(i/8)) for i in [912, 888, 928, 392, 408])).encode()))})')
                
```

website for obfuscation [https://pyobfuscate.com/pyd]
[[S2Day6Net.md]]

