import sys
import time

def xor_string(input_string, key):
    return ''.join((chr(ord(char) ^ ord(key[i % len(key)])) for i, char in enumerate(input_string)))

def to_hex(input_string):
    return ''.join((f'{ord(char):02x}' for char in input_string))

def from_hex(hex_string):
    return ''.join((chr(int(hex_string[i:i + 2], 16)) for i in range(0, len(hex_string), 2)))

checkmeout = '6a7b726d75030d48520d0452516c5c0a6c005f6c4809466e5a075f66000108014c'
decoded_input = from_hex(checkmeout)

for i in range(1000):
    key = str(i)
    decrypted = xor_string(decoded_input, key)
    if 'CTF' in decrypted:
        print(f"Decrypted String: {decrypted}")
        break

# SHCTF24{c47ch_m3_1f_y0u_c4n_3012}