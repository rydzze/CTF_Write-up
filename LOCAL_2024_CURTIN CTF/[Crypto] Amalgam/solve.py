from Crypto.Util.number import inverse, long_to_bytes
from sympy import discrete_log

def decrypt(c1, c2, p, g, h):
    y = discrete_log(p, c1, g)

    h_y = pow(h, y, p)
    h_y_inv = inverse(h_y, p)

    m = (c2 * h_y_inv) % p
    return m

p = 186506814954895414068796533711441426871
g = 2
h = 128780011407215156870232600336696679553
c1 = 156581689710555992734938659724336258165
c2 = 113787733820173627914147318932861607685

m = decrypt(c1, c2, p, g, h)

flag = long_to_bytes(m)
print(flag.decode('utf-8'))

# CURTIN_CTF{dlP_50lv3d:)}