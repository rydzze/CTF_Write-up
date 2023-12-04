#!/usr/bin/env sage
import string
SET = "ABOH23{}_!?" + string.ascii_lowercase + string.digits
n = len(SET)

def encrypt(msg, f):
    ct = ''
    for c in msg:
        ct += SET[f.substitute(SET.index(c))]
    return ct

P.<x> = PolynomialRing(GF(n))
f = P.random_element(4)

FLAG = open('../flag.txt', 'r').read().strip()

enc = encrypt(FLAG, f)

with open('out.txt', 'w') as f:
    print(enc)
    f.write(enc)