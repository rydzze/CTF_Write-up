"""
RSA 2

@author: RDxR10
"""

from Crypto.Util.number import bytes_to_long

import random
from math import gcd


def generate_close_primes(bits):
    p = random.getrandbits(bits)
    if p % 2 == 0:
        p += 1
    while not is_prime(p):
        p += 2
    q = p + 2
    while not is_prime(q):
        q += 2
    return p, q

def is_prime(n, k=5):
    if n < 2: return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        if n % p == 0: return n == p
    s, d = 0, n - 1
    while d % 2 == 0:
        s, d = s + 1, d // 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1: continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1: break
        else:
            return False
    return True

def generate_keys(bits):
    p, q = generate_close_primes(bits // 2)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = pow(e, -1, phi)
    print("p:", p)
    print("q:", q)
    return (n, e), (n, d)

def encrypt(message, public_key):
    n, e = public_key
    return pow(message, e, n)

# Example usage
bits = 1024
public_key, private_key = generate_keys(bits)
message = bytes_to_long(b'REDACTED')
encrypted = encrypt(message, public_key)
print(f"Encrypted message: {encrypted}")
print(public_key)