def enc_shift(n: int, bits: int, shift: int, direction: str = 'left') -> int:
    bit_len = bits
    
    if direction == 'left':
        return ((n << shift) | (n >> (bit_len - shift))) & ((1 << bit_len) - 1)
    elif direction == 'right':
        return ((n >> shift) | (n << (bit_len - shift))) & ((1 << bit_len) - 1)
    else:
        raise ValueError("Something's not right\n")

flag = []
shifted = [153, 27, 133, 217, 237, 146, 49, 14, 49, 210, 9, 153, 153, 205, 145, 157, 212, 221, 193, 157, 9, 82, 228, 21, 13, 215, 185, 219, 125, 152, 165, 29, 205, 215, 177, 12, 212, 205, 245]
bits = 8

for i in range(len(shifted)):
    if (i%2 != 0):
        flag.append(enc_shift(shifted[i], bits, 2, 'left'))
    else:
        flag.append(enc_shift(shifted[i], bits, 2, 'right'))

flag = ''.join(chr(flag[i]) for i in range(len(flag)))
print(flag)

# flag{JL8LKBff7dv5wpvBI9TC_no_bits_l057}