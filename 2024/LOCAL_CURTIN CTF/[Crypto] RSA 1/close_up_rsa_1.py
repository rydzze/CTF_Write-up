"""
RSA 1

@author: RDxR10
"""

import random
from Crypto.Util.number import bytes_to_long

def gen_primes(bits, c_f):
    
    p = random.getrandbits(bits)
    if p % 2 == 0:
        p += 1
    while not is_prime(p):
        p += 2
    
    
    lower_bound = p + (p // c_f)
    upper_bound = p + (p // (c_f // 2))
    q = random.randint(lower_bound, upper_bound)
    if q % 2 == 0:
        q += 1
    while not is_prime(q):
        q += 2
        if q > upper_bound:
            q = lower_bound
            if q % 2 == 0:
                q += 1
    
    return p, q

def is_prime(n, k=5):
    if n < 2: return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
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


p, q = gen_primes(4096, 9998)
n = p * q
phi = (p - 1) * (q - 1)
e = 65537
d = pow(e, -1, phi)
m = b'REDACTED'
c = pow(bytes_to_long(m), e, n)

print(f"n = {n}")
print(f"|p - q| = {abs(p - q)}")
print(f"c = {c}")
print(f"e = {e}")