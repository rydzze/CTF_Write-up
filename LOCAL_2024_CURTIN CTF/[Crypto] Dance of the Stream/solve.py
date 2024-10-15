import struct

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

def decrypt(encrypted_message, obfuscated_nonce):
    nonce = struct.unpack("<Q", o_value(obfuscated_nonce))[0]
    
    for key_value in range(65536):
        prng_key = struct.pack("<H", key_value)
        m = stream_e(prng_key, nonce, encrypted_message)
        
        try:
            flag = m.decode('utf-8')
            if "CURTIN_CTF" in flag:
                print(f"Found key: {key_value}")
                print(flag)
                break
        except UnicodeDecodeError:
            continue

if __name__ == "__main__":
    with open("ciphertext.txt", "rb") as f:
        encrypted_message = f.read()

    with open("o_nonce.txt", "rb") as f:
        obfuscated_nonce = f.read()
    
    decrypt(encrypted_message, obfuscated_nonce)

# CURTIN_CTF{g0_s0lv3_7h3_57r34m_pr0bl3m_0f_1r0d0v_n0w}