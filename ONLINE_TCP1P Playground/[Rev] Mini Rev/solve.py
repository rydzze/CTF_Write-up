enc_flag = [0x22, 0x61, 0xC9, 0xC3, 0x41, 0x1C, 0x93, 0x0F, 0x18, 0x4B, 0xC6, 0x80, 0x74, 0x11, 0xA1, 0x00, 0x19, 0x50, 0xC6, 0x9F, 0x78, 0x09, 0x97, 0x39, 0x15, 0x4A, 0xF8, 0x9E, 0x7D, 0x02, 0x90, 0x01, 0x13, 0x7D, 0xC1, 0xB6, 0x6C]
key = [0x76, 0x22, 0x99, 0xf2, 0x11, 0x67, 0xfe, 0x66]
    
flag = ''.join(chr(enc_flag[i] ^ key[i % len(key)]) for i in range(len(enc_flag)))

print(flag)