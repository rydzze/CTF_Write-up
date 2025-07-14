def init_remap():
    remap = {
        'a': 'q', 'b': 'w', 'c': 'e', 'd': 'r', 'e': 't', 'f': 'y', 'g': 'u',
        'h': 'i', 'i': 'o', 'j': 'p', 'k': 'a', 'l': 's', 'm': 'd', 'n': 'f',
        'o': 'g', 'p': 'h', 'q': 'j', 'r': 'k', 's': 'l', 't': 'z', 'u': 'x',
        'v': 'c', 'w': 'v', 'x': 'b', 'y': 'n', 'z': 'm'
    }
    return {v: k for k, v in remap.items()}

map = init_remap()

flag = "".join(map.get(i, i) for i in "L3AK{ngx_qkt_fgz_ugffq_uxtll_dt}")
print("Flag:", flag)
