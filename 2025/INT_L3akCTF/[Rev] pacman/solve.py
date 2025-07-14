from struct import unpack, pack

def rol(val, r_bits, max_bits=64):
    return ((val << r_bits) & (2**max_bits - 1)) | (val >> (max_bits - r_bits))

def transform(right, key):
    x = right ^ key
    tmp = rol(x, 13)
    result = ((x << 5) - x) ^ tmp
    return result & 0xFFFFFFFFFFFFFFFF

keys = [0x00001337deadbeef, 0x0000c0de12345678,
        0x0000abcdef012345, 0x00009876543210ab]

enc = bytes([
    0x91, 0xbc, 0x04, 0x8f, 0x7a, 0x48, 0x83, 0xfd,
    0x31, 0x63, 0x41, 0x16, 0x93, 0xb2, 0xa9, 0x1e,
    0x4f, 0x94, 0x08, 0x6b, 0x54, 0xa4, 0xbe, 0x2f,
    0xaf, 0xdc, 0x54, 0x98, 0x7e, 0x9e, 0x2e, 0x92
])

blocks = [enc[i:i+16] for i in range(0, 32, 16)]
flag = b""

for block in blocks:
    L = unpack("<Q", block[:8])[0]
    R = unpack("<Q", block[8:])[0]

    for i in reversed(range(4)):
        L, R = R, L
        L ^= transform(R, keys[i])

    flag += pack("<Q", L) + pack("<Q", R)

print("Flag:", flag.decode())
