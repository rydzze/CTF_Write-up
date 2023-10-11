## Strings in the Binary

### 📚Overview

Change the hex value in `obscured_flag.bin` to get the flag from the decoded text by using HxD (Hex Editor).

### ✨ Solution

Open the file and you will find that the flag is incomplete. It looks like the hex value represents the ASCII characters.

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/a137cbc0-ab72-40d9-8994-39975a5137a0)

Since we know the format of the flag is `petgrad2023{xxxxx}`, here is what I came up with:
- Increase the hex value by 20 if the decoded text is an uppercase letter, symbol, or blank.
- Decrease the hex value by 20 if the decoded text is a lowercase letter.

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/546b6249-b17a-4918-8356-093f07be2109)

### 🏳️ Flag

Hence, the flag is `petgrad2023{B1nary_Exp10r3r}` 
