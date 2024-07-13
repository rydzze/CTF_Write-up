## Baby Reverse

### 📚 Overview

Reverse it, but not using "strings".

### ✨ Solution

First, let's look at what type of file babyrev is using the command `file babyrev`.

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/cd4e5ece-f1ae-4319-8599-2a9613232b26)

It is .ELF 64-bit file so let's hop on [Ghidra](https://ghidra-sre.org/) and decompile it.

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/7112129a-c8c0-4b42-8ce4-186ebf3f6668)

Referring to the picture above, double-click on the variable `flag` and then copy the grey text. After that, do some cleaning and the flag is yours :D.

### 🏳️ Flag

Hence, the flag is `WSCTF2021{R3ver5e_1s_EzPz}`
