ENC_KEY = [0x5B, 0x3E, 0x42, 0x13, 0x3B, 0x33, 0x48, 0x29]
ASCII_START = 0x21
ASCII_END = 0x7e

key = ''
for i in range(len(ENC_KEY)):
    for char in range(ASCII_START, ASCII_END):
        guess = (char * (i+1) + 0xd) % 0x61 
        if guess == ENC_KEY[i]:
            key += chr(char)
            break

print("Key:", key)
