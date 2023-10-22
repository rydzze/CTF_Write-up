enc = [0x0f, 0x63, 0x11, 0x60, 0x0a, 0x03, 0x56, 0x01, 0x10, 0x06]
key1 = "WSCTF2021{"

key1_ascii = [ord(char) for char in key1]

# XOR enc with key1's ASCII values
key2 = []
for i in range(len(enc)):
    key2.append(enc[i] ^ key1_ascii[i % len(key1_ascii)])

# Convert the result back to a string
key2 = ''.join([chr(byte) for byte in key2])

print("flag: ", key1+key2)
