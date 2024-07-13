mask = 0xFFFFFFFF #act as a bit mask to preserve only 32 bits from the result

def rightRotate(value, shift):
    shift = shift % 32  # Ensure the shift is within 0-31
    # Perform the right rotate operation
    result = ((value >> shift) | (value << (32 - shift))) & mask
    return result

def XOR(param1, param2):
    result = (param1 ^ param2) & mask
    return result

def subtract(param1, param2):
    if param1 < param2:
        param1 += 0x100000000
    result = param1 - param2
    return result 

enc = 0x467BB09B

flag = XOR(enc, 0xBA14C823)
flag = rightRotate(flag, 5)
flag = subtract(flag, 0xD1507BA)
flag = XOR(flag, 0xAAFBBCBE)
flag = subtract(flag, 0x45370DF7)

print(str(hex(flag)[2:]).upper())
