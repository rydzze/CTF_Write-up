## GDB basics

### 📚 Overview

https://www.sourceware.org/gdb/documentation/

### ✨ Solution

```bash
┌──(kali@kali)-[~/Downloads]
└─$ ./a.out
Enter a number : 1
I cannot provide you a flag !
```

When we run the programme, it will ask for a number and if it is correct, then the flag will be displayed.
As the chall's title stated "GDB", let's use `gdb` to debug the programme to get the correct number.

Disassemble the main function by using the `disassemble main` command.

![image](https://github.com/rydzze/Crackmes_Solution/assets/86187059/e76eb9ab-902a-439b-86be-237987d3bae7)

Before the programme asks for user input, we can see that it processes mathematical operations to generate the number.
Later, the programme will compare our input with the generated number, which is stored in `EAX / [rbp-0x4]`.

To ease our job, create a breakpoint at `main+44` using `break *main+44` command, run the programme and inspect the content of `EAX` register.

![image](https://github.com/rydzze/Crackmes_Solution/assets/86187059/03b03059-b782-47db-bfc2-ce66de1d8d3a)

It appears that the generated number is `0xd120000` which is `219283456` in base 10. Insert the number and the flag is yours.

### 😼 Shortcut

Create a breakpoint at `main`, run the programme and when it stops at `main`, use `jump main+93` command to get the flag. 

### 🏳️ Flag

Hence, the flag is `I_LOVE_YOU`.
