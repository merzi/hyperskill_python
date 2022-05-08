encoded = input()
key = sum(int(input()).to_bytes(2, byteorder='little'))

decoded = ""
for char in encoded:
    decoded += chr(ord(char) + key)

print(decoded)
