## ex02

### ✨ Solution

Run `file ex02.exe` command and we will find that it is a PE32 executable. Let's debug the file using [x32dbg](https://x64dbg.com/) because it is 32-bit.

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/39ed1937-89dd-492d-9b5c-dd2212e1ba45)

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/e864e6e3-1125-4330-84d3-bd27d2e84959)

Look at the Assembly code (highlighted in the image above), the programme will ask the user for input through `call ex02.DF1334`.
Then, it will encrypt the input using mathematical and logical operations and compare it with `0x467BB09B`.
If it is equal, then the input (which is our flag btw) is correct.

During the competition, I solved it manually (tedious process lmao). In this write-up, I did a Python code to solve it so check it out :D.

_P.S.: You need basic fundamentals of computer architecture to understand it (basic is enough, don't worry)_

### 🏳️ Flag

Hence, the flag is `CAFEBABE`.
