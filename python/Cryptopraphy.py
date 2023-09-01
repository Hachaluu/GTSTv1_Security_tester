def encrypt():
	msg=input("Message: ")
	key=input("key: ")
	encrypt_hex = ""
	key_itr=0
	for i in range(len(msg)):
		deciText=ord(msg[i]) ^ ord(key[key_itr])
		key_itr+=1
		if key_itr>=len(key):
			key_itr=1
		encrypt_hex += hex(deciText)[2:]
	print(f"Message Encrypted Sucssfully!\nMessage: {encrypt_hex}")

def decrypt():
	msg=input("Message: ")
	key=input("key: ")
	hex2uni = ""
	key_itr = 0 
	decrypt_text = ""
	for i in range(0,len(msg),2):
		hex2uni+=bytes.fromhex(msg[i:i+2]).decode('utf-8')
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