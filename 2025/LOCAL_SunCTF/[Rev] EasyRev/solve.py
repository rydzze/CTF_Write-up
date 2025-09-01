# ROT13 implementation for alphabets
def rot13(b):
    if 65 <= b <= 90:
        return (b - 65 + 13) % 26 + 65
    elif 97 <= b <= 122:
        return (b - 97 + 13) % 26 + 97
    return b

# ROT47 implementation for printable ASCII characters (33-126)
def rot47(b):
    if 33 <= b <= 126:
        return 33 + ((b - 33 + 47) % 94)
    return b

def decode_ciphertext(ct):
    data = [ord(c) for c in ct]
    data = [(b + 23) % 256 for b in data]

    data = [b ^ 232 for b in data]
    data = [(b - 217) % 256 for b in data]

    data = [rot47(b) for b in data]
    data = [rot13(b) for b in data]

    return ''.join(chr(b) for b in data)

if __name__ == "__main__":
    ciphertext = "áãÌÛâÞ»¾¶ºâ¾Êâà¼Ê½ß¼Ê¹ÞÊ½ºÊÌ¹å¸"
    flag = decode_ciphertext(ciphertext)

    print("[+] Decrypted Flag:", flag)
