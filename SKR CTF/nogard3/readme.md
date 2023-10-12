## nogard2

### 📚 Overview

Ghidra reversing challenge 3!
Not so easy for this one hehe..

### 🤔 Hint 

> _"Math is the key!"_

### ✨ Solution

Open the file using [IDA tool](https://hex-rays.com/ida-free/), decompile it and then press F5 to look at the source code.

```C
int __fastcall main(int argc, const char **argv, const char **envp)
{
  unsigned int v4; // [rsp+18h] [rbp-18h] BYREF
  unsigned int v5; // [rsp+1Ch] [rbp-14h] BYREF
  unsigned int v6; // [rsp+20h] [rbp-10h] BYREF
  unsigned int v7; // [rsp+24h] [rbp-Ch] BYREF
  unsigned __int64 v8; // [rsp+28h] [rbp-8h]

  v8 = __readfsqword(0x28u);
  printf("Enter code: ");
  __isoc99_scanf("%x-%x-%x-%x", &v4, &v5, &v6, &v7);
  if ( 3 * v7 + v4 == 0xad8 && 3 * v6 * v5 == 0x132b340 && v4 == 0x133 && v7 + 0x123 * v6 == 0xf01ea )
    printf("Correct code! The flag is SKR{%x%x%x%x}\n", v4, v5, v6, v7);
  else
    puts("Wrong code..");
  return 0;
}
```

If we look at the if-else statement, there are four conditional statements that we have to follow where
- `3 * v7 + v4 == 0xad8`
- `3 * v6 * v5 == 0x132b340`
- `v4 == 0x133`
- `v7 + 291 * v6 == 0xf01ea`

Since we are given the value of `v4`, we can calculate the value of `v5, v6, and v7`.

```C
3 * v7 + v4 = 0xad8      3 * v6 * v5 = 0x132b340      v7 + 0x123 * v6 = 0xf01ea
     v7 * 3 = 0x9a5          v6 * v5 = 0x663bc0            0x123 * v6 = 0xefeb3
         v7 = 0x337               v5 = 0x7c0                       v6 = 0xd31
```

Then, combine all parts together with changing the hex value

### 🏳️ Flag

Hence, the flag is `SKR{1337c0d31337}` 
