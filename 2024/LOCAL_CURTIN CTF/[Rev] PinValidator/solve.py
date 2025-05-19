enc_flag = "^\"u}B~%F'\"x%bU&r%dZ'p%P&d%`%d"

flag = ''.join(chr(ord(enc_flag[i]) ^ 22) for i in range(len(enc_flag)))
flag = 'CURTIN_CTF{' + flag + '}'

print(flag)

# CURTIN_CTF{H4ckTh3P14n3tC0d3rL1f3F0r3v3r}