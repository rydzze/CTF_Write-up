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

### 🤬 My Argument

In my opinion, the PIN number of the safe box should not be 89076 because it doesn't pass the checking. Let's take a look at the function graph.

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/0f129328-2b56-4a69-a382-a99e29140b6b)

We could see that `r16, r17, r18, r19, r20` are loaded into `R18, R20, R22, Zlo, Xlo` and `loop::userPin, DAT_mem_0188, DAT_mem_0189, DAT_mem_018a, DAT_mem_018b` are loaded into `R25, R19, R21, R23, Zhi` respectively. After that, the Assembly code moves the content of `R7` into `R24` and then it's gonna compare `R25, R19, R21, R23, Zhi` with `R24, R18, R20, R22, Zlo` respectively. 

However, `Xlo` that holds the content of `r20`, which is 6 (the last digit of the PIN number) is not present in the comparison and there is a new number that was supposed to be a part of the PIN number as the first digit which is `R24` that holds the content of `R7`. Thus, we could say 89076 is the incorrect PIN. 

Then, what is the PIN number of the safe box? Let's take a look at the decompiled source code. 

```C
if ((((loop::userPin != R7) || (DAT_mem_0188 != r16)) || (DAT_mem_0189 != r17)) ||
   ((DAT_mem_018a != r18 || (DAT_mem_018b != r19)))) {
  R25R24._0_1_ = '\0';
}
if ((byte)R25R24 == '\0') {
  R25R24 = s_Incorrect_PIN._Try_again._mem_016b;
}
else {
  R25R24 = s_Locker_unlocked!_You_entered_the_mem_013d;
}
```

In the first if-else statement, we see that there are 5 conditional statements. If any of these conditional statements are true (which means the user input is not equal to the actual PIN), the PIN number is incorrect.

Assuming that `loop::userPin, DAT_mem_0188, DAT_mem_0189, DAT_mem_018a, DAT_mem_018b` is the user input, then `R7, r16, r17, r18, r19` should be the PIN number of the safe box. Since we know that the values for `r16 = 8, r17 = 9, and r19 = 7`, we need to find the values of `R7` and `r18` to complete the PIN number, _89_7.

In line 83 of the decompiled source code, we can see that the variable `R7` is assigned with a value `'\x01'` which is 1 in hexadecimal thus making the PIN number 189_7. Hence, we can do trial and error to unlock the safe box. By any chance if `r18 = 0` just like in the Solution section, then the PIN number is 18907. 
