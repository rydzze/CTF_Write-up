import itertools
def a(b):
    if 65 <= b <= 90:
        return (b - 65 + 13) % 26 + 65
    elif 97 <= b <= 122:
        return (b - 97 + 13) % 26 + 97
    return b
def g(b):
    if 33 <= b <= 126:
        return 33 + ((b - 33 + 47) % 94)
    return b
def c(d, k1):
    return [(b ^ k1) for b in d]
def h(d, k1):
    return [(b + k1) % 256 for b in d]
def e(d, k1):
    return [(b - k1) % 256 for b in d]
tt = {
    'a': lambda: lambda d: [a(b) for b in d],
    'g': lambda: lambda d: [g(b) for b in d],
    'c':   lambda k: lambda d: c(d, k),
    'h':   lambda k: lambda d: h(d, k),
    'e':   lambda k: lambda d: e(d, k),
}
def bb(ct: str):
    ob = [ord(c) for c in ct]
    o = ['a', 'g', 'c', 'h', 'e']
    for d in range(1, 6):
        for ops in itertools.permutations(o, d):
            kp = [i for i, op in enumerate(ops) if op in {'c', 'h', 'e'}]
            ks = range(256) if kp else [None]
            print("Debug!")
            for k2 in itertools.product(ks, repeat=len(kp)):
                try:
                    d = ob.copy()
                    k1_idx = 0
                    for i, op in enumerate(ops):
                        if op in {'c', 'h', 'e'}:
                            k1 = k2[k1_idx]
                            k1_idx += 1
                            t = tt[op](k1)
                        else:
                            t = tt[op]()
                        d = t(d)
                    r = ''.join(chr(b) for b in d)
                    if r.startswith("sunctf25{"):
                        return r
                except:
                    continue
    print("[-] No flag found.")
    return None
if __name__ == "__main__":
    ct = "áãÌÛâÞ»¾¶ºâ¾Êâà¼Ê½ß¼Ê¹ÞÊ½ºÊÌ¹å¸"
    bb(ct)