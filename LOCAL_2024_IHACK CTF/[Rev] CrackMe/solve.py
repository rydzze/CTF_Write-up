hidden = "BRQFHF@WR_+6 ,N:$78"
key = "secret"

for i in range(len(hidden)):
    print(chr(ord(hidden[i]) ^ ord(key[i % len(key)])), end='')