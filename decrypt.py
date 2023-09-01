def encrypt():
    msg=input("message: ")
    key=input("key: ")
    encrypt_hex = ""
    key_itr=0
    for i in range(len(msg)):
        deciText=ord(msg[i]) ^ ord(key[key_itr])
        key_itr+=1
        if key_itr >= len(key):
            key_itr=0 
        encrypt_hex += hex(deciText) [2:]
    print(f"The message was decrpted!\nmessage: {encrypt_hex} ")

encrypt()