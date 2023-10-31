import gdb
#gdb -q -x otp.py

gdb.execute("file ./otp")
gdb.execute("run " + ('1'*100))
gdb.Breakpoint("strncmp@plt")
hexa = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
key = "" #6fa2e2a25c3b5869d75c7a5a062a4a51194c451e663fff306668ec42212a341f40cd199d78c72a21481596117a7c5e5217ac

for i in range(100):
    for char in hexa:
        keyLen = len(key)
        gdb.execute("run " + key + (char * (100 - keyLen)))
        rsi = gdb.execute("x/s $rsi", to_string = True)
        rsi = rsi[17:117]
        rdi = gdb.execute("x/s $rdi", to_string = True)
        rdi = rdi[17:117]

        if rsi[keyLen] == rdi[keyLen]:
            key += char
            break
        elif len(rsi) > 0 and rsi[keyLen] == rsi[keyLen-1]:
            key += '0'
            break

print(key)