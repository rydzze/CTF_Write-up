#!/usr/bin/env sage
from Crypto.Util.number import bytes_to_long

p, q = random_prime(2 ^ 1024), random_prime(2 ^ 1024)
n = p*q
e = 3

assert len(flag) > e

FLAG = open("flag.txt", "rb").read().strip()
m = bytes_to_long(FLAG + b' is your challenge flag.')

c = pow(m, e, n)

print("N: ", n)
print("C: ", c)
print("e: ", e)