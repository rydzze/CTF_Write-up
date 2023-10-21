## Show Flag

### 📚 Overview

Open the app to show the flag!

### ✨ Solution

When we run the `showflag.exe`, it will give us one out of the five images randomly.

Now, open the `showflag.exe` in [dnSpy](https://github.com/dnSpy/dnSpy) and look at the class `flags` (refer to the image below).

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/ce1d125e-ef33-4e8d-a962-92c56534009b)

It looks like we are only calling for the `flag1`, `flag2`, `flag3`, `flag4`, `flag5` while `donotopen` and `flag6` is not called.
What we can do is edit the IL instructions of class `flags` to retrieve `donotopen` and `flag6`.  

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/6760e6be-1585-4fb6-a144-5aecfaaf5059)

Left-click on the operand with the opcode "call", choose Method and then pick `donotopen` and `flag6`.
It is going to look like this, depending on your preferences ;).

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/570ce2fe-aa42-4558-913d-24f766f09d85)

Press OK and then `Ctrl + Shift + S` to save all the changes made to the `showflag.exe` file. Next, run it.

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/79de8aa3-cbc7-4070-a5ae-33dd47aabff9)

Congratulations! You just got rickrolled XD.

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/5641da5d-c298-4d2b-b7bf-96d66d09f6de)

Ohhh nevermind, here is the flag.

### 🏳️ Flag

Hence, the flag is `WSCTF2021{XOR1NG_1M4G35}`
