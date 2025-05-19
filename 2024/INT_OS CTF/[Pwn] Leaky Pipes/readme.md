# [Pwn] Leaky Pipes

## 📚 Overview

> *"Welcome to Leaky Pipes, where a seemingly innocent program has sprung a serious leak! Your mission is to uncover the concealed flag hidden within the program. Will you be the one to patch the leak and reveal the hidden secret?"*

## 🔎 *Reconnaissance*

[Format string](https://ctf101.org/binary-exploitation/what-is-a-format-string-vulnerability/) vulnerability, the programme directly passed the `local_cc` var to the `printf` w/o any format specified.

```c
void vuln(void){
  char local_cc [128];
  undefined local_4c [68];
  
  readflag(local_4c,0x40);
  printf("Tell me your secret so I can reveal mine ;) >> ");
  __isoc99_scanf("%127s",local_cc);
  puts("Here\'s your secret.. I ain\'t telling mine :p");
  printf(local_cc);
  putchar(10);
  return;
}
```

## ✨ Solution

Let's spam the `%p` as input to print the pointer/address stored inside the variable. The programme will print out the hexadecimal numbers stored in little endian format and then we can retrieve the flag from the output. Use [CyberChef](https://gchq.github.io/CyberChef/) to decode it.

## 🏳️ Flag

`OSCTF{F0rm4t_5tr1ngs_l3ak4g3_l0l}`