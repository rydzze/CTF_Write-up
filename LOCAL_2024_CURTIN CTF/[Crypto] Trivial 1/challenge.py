"""
Trivial 1

@author: RDxR10
"""


from Crypto.Util.number import getPrime
import random


def generate_large_prime(bits):
    return getPrime(bits)


prime_list = [generate_large_prime(512) for _ in range(7)]

def encrypt(flag, primes, key):
    encrypted_values = []
    for char in flag:
        ascii_val = ord(char)
        encrypted_val = ascii_val
        for prime in primes:
            encrypted_val = (encrypted_val * prime) ^ key
        encrypted_values.append(encrypted_val)
    return encrypted_values



flag = "REDACTED"
key = random.randint(1, 100)
encrypted = encrypt(flag, prime_list, key)

print(f"Encrypted flag: {encrypted}")
print(f"Prime list: {prime_list}")