# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: iamspeed.py
# Bytecode version: 3.10.0rc2 (3439)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import sys
import time

def xor_string(input_string, key):
    return ''.join((chr(ord(char) ^ ord(key[i % len(key)])) for i, char in enumerate(input_string)))

def to_hex(input_string):
    return ''.join((f'{ord(char):02x}' for char in input_string))

def from_hex(hex_string):
    return ''.join((chr(int(hex_string[i:i + 2], 16)) for i in range(0, len(hex_string), 2)))
checkmeout = '5c404344470d1b1b445c5b45404145581a56401b766472604d'
decoded_input = from_hex(checkmeout)
for i in range(1000):
    key = str(i)
    decrypted = xor_string(decoded_input, key)
    sys.stdout.write(f'\rDecrypted String: {decrypted}0')
    sys.stdout.flush()
    time.sleep(0.01)
print()
print('Did you checked properly? Its somewhere on the web..')