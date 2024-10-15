# -*- coding: utf-8 -*-
"""
Dance of the Stream

author: @RDxR10
"""

import struct, random


ROUNDS = 20

def q_r(a, b, c, d):
    a = (a + b) & 0xFFFFFFFF
    d = (d ^ a) << 16 | (d ^ a) >> (32 - 16)
    c = (c + d) & 0xFFFFFFFF
    b = (b ^ c) << 12 | (b ^ c) >> (32 - 12)
    a = (a + b) & 0xFFFFFFFF
    d = (d ^ a) << 8 | (d ^ a) >> (32 - 8)
    c = (c + d) & 0xFFFFFFFF
    b = (b ^ c) << 7 | (b ^ c) >> (32 - 7)
    return a, b, c, d

def stream(key, nonce, counter):
    state = [0] * 16
    state[0] = 0x61707865
    state[1] = 0x3320646e
    state[2] = 0x79622d32
    state[3] = 0x6b206574
    state[4:6] = struct.unpack("<2L", key + b'\x00' * 6)
    state[6:8] = [0] * 2
    state[8:12] = [0] * 4
    state[12] = counter
    state[13] = nonce & 0xFFFFFFFF
    state[14] = (nonce >> 32) & 0xFFFFFFFF
    state[15] = 0

    working_state = state[:]
    for _ in range(ROUNDS // 2):
        working_state[0], working_state[4], working_state[8], working_state[12] = q_r(
            working_state[0], working_state[4], working_state[8], working_state[12]
        )
        working_state[1], working_state[5], working_state[9], working_state[13] = q_r(
            working_state[1], working_state[5], working_state[9], working_state[13]
        )
        working_state[2], working_state[6], working_state[10], working_state[14] = q_r(
            working_state[2], working_state[6], working_state[10], working_state[14]
        )
        working_state[3], working_state[7], working_state[11], working_state[15] = q_r(
            working_state[3], working_state[7], working_state[11], working_state[15]
        )
        working_state[0], working_state[5], working_state[10], working_state[15] = q_r(
            working_state[0], working_state[5], working_state[10], working_state[15]
        )
        working_state[1], working_state[6], working_state[11], working_state[12] = q_r(
            working_state[1], working_state[6], working_state[11], working_state[12]
        )
        working_state[2], working_state[7], working_state[8], working_state[13] = q_r(
            working_state[2], working_state[7], working_state[8], working_state[13]
        )
        working_state[3], working_state[4], working_state[9], working_state[14] = q_r(
            working_state[3], working_state[4], working_state[9], working_state[14]
        )

    output = bytearray()
    for i in range(16):
        output.extend(struct.pack("<L", (working_state[i] + state[i]) & 0xFFFFFFFF))
    return output

def stream_e(key, nonce, message):
    keystream = bytearray()
    for i in range(0, len(message), 64):
        keystream.extend(stream(key, nonce, i // 64))
    
    return bytes([m ^ k for m, k in zip(message, keystream)])

def o_value(value):
    o_kie = b'leomessi'
    return bytes([b ^ o_kie[i % len(o_kie)] for i, b in enumerate(value)])

class PRNG:
    def __init__(self, seed):
        self.state = seed
        self.update()

    def update(self):
        self.state = (self.state * 0x5DEECE66D + 0xB) & 0xFFFFFFFFFFFF
        self.state ^= self.state >> 33
        self.state = (self.state * 0xFF51AFD7ED558CCD + 0xC4CEB9B11F7A6F8D) & 0xFFFFFFFFFFFF

    def get_bytes(self, num_bytes):
        result = bytearray()
        for _ in range(num_bytes):
            self.update()
            result.append(self.state & 0xFF)
        return bytes(result)

def main():
    nonce = random.getrandbits(64)
    message = b'REDACTED'
    prng = PRNG(random.randint(1, 9999999999999999999999999999999999999999999999))
    prng_key = prng.get_bytes(2)
    encrypted_message = stream_e(prng_key, nonce, message)
    with open("ciphertext.txt", "wb") as f:
        f.write(encrypted_message)
    
    o_nonce = o_value(struct.pack("<Q", nonce))
    with open("o_nonce.txt", "wb") as f:
        f.write(o_nonce)

if __name__ == "__main__":
    main()