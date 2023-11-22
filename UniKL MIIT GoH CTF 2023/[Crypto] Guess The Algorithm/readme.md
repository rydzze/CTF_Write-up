## Guess The Algorithm

### 📚 Overview

![Guess the algorithm](https://github.com/rydzze/CTF_Write-up/assets/86187059/b0c3b2a2-8e21-4249-bc70-3fc44da9bb34)

### ✨ Solution

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/dc88cef6-981b-49d8-b014-8bb86eeb2b13)
*_disassemble using Ghidra_

We have to guess what kind of encryption method it uses and it will print the key.
Since the **filetype** of the given file is `.ELF` and there is **strcmp** (string compare) in the code, I just **debug** it using `gdb-peda` hoping something pops up.

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/952812ab-5bb6-4ccd-966a-dd6f9f883583)
*_disassemble main function using gdb-peda_

Insert **breakpoint** anywhere **before strcmp@plt** and **input stream**, so I add at 0x00005555555552ed, `b * main+260`. Run it.

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/e29388fd-f2d7-45c4-be45-6c1eb92d0bec)
![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/71287e76-0b97-4987-941f-9a169e087b11)

### 🏳️ Flag

Hence, the flag is `gohunikl2023{LicielaWasHere}` 
