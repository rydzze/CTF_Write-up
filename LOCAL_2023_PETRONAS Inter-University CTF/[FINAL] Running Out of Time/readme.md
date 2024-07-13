## Running Out of Time

### 📚 Overview

The flag is locked inside a safe box! Find the PIN number to access it by reading the ELF file using a reverse engineering tool. 

### ✨ Solution

We are given the `runningoutoftime1.elf` file and we have to find the PIN number in it. So, let's hop on `Ghidra` to read the ELF file.

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/1b7f2e0f-33fe-4cc6-a5a5-d222a59baf64)

If we look at the Assembly code of the ELF file, we can see that the first 10 lines in `LAB_code_0002f1` are loading the data directly from the data space. Assuming that the first 5 lines are the actual PIN while the second 5 lines are user input, these two will be compared to verify whether the user input is equal to the actual PIN number.

Look at the right side of the first 5 lines of Assembly code (the grey text) OR hover your cursor over `r16/r17/r19`, we can see that they are already assigned undefined values which are 8, 9, 7, and 6. Now, we need to find the third digit to complete the PIN number, 89_76. Since there are only 10 possible outcomes (0-9), we could do trial and error to unlock the safe box. Eventually, you will unlock it on the first try with the PIN number 89076 and the flag is yours!

### 🏳️ Flag

The flag is inside the safe box :)