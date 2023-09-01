import base64
message = input("Text: ")
encoded = base64.b64encode(bytes(message,'utf-8'))
print(f"Sucessufully encoded!\n >> {encoded}")

decoded = base64.b64decode(encoded)
print(f"Sucessfully decoded!\n >> {decoded}")