# [Rev] iamspeed

## 📚 Overview

> *"__ . Anyways, the flag is somewhere in the code. Its all there"*

## ✨ Walkthrough

Given .EXE file written in Python ... how? the icon of the file is a *dead giveaway* lol. Since Python is a *hybrid programming language*, we can retrieve back the original source code :D.

### 1. Converting Python .EXE into Python bytecode .PYC 

Utilise the tool [PyInstaller Extractor](https://github.com/extremecoders-re/pyinstxtractor) to convert the executable file into the bytecode. 

### 2. Converting Python bytecode .PYC into Python source code .PY

Since we cannot decompile it using [uncompyle6](https://pypi.org/project/uncompyle6/), we can use the web tool [PyLingual](https://pylingual.io/) to retrieve the source code.

```python
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
```

### 3. Analyse the Source Code

It looks like the source code will decrypt the hex string for a thousand times and the hint given implying that *the flag is somewhere on the web*. I did a modification on the write statement by changing `sys.stdout.write(f'\rDecrypted String: {decrypted}0')` to `print(f'\rDecrypted String: {decrypted}')` so that we could observe the output. Turns out there is a link which led us to flag.txt, which contain another hex string. To decrypt it, insert the new hex string in checkmeout variable and print the decrypted string if its contain CTF in it.

## ⚙ Script

```python
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
```

## 🏳️ Flag

`SHCTF24{c47ch_m3_1f_y0u_c4n_3012}`