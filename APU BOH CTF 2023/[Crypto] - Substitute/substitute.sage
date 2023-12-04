#!/usr/bin/env sage
import string, base64, math

flag = open('../flag.txt', 'rb').read()

SET = string.printable[:62] + '\\='

R = list(GF(64))

def keygen(l):
    key = [R[randint(1, 63)] for _ in range(l)] 
    key = math.prod(key) # Optimization the key length :D
    return key

def substitute(c):
    assert c in SET
    return R[SET.index(c)]

def encrypt(msg, key):
    m64 = base64.b64encode(msg)
    enc, pkey = '', key**1337
    for m in m64:
        enc += SET[R.index(pkey * substitute(chr(m)))]
    return enc

def rnaencode(msg):
    binstr = ''.join(format(byte, '08b') for byte in msg.encode())
    print(binstr)
    rna = []
    for i in range(0, len(binstr), 2):
        if binstr[i:i+2] == "00":
            rna.append("A")
        elif binstr[i:i+2] == "01":
            rna.append("C")
        elif binstr[i:i+2] == "10":
            rna.append("G")
        elif binstr[i:i+2] == "11":
            rna.append("U")
    return ''.join(rna)

key = keygen(16)
print(key)

enc = encrypt(flag, key)

with open('out.txt', 'w') as f:
    f.write(rnaencode(enc))