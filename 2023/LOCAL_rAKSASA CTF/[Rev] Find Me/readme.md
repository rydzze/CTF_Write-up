## Find Me

### 📚 Overview

Find me

### ✨ Solution

First, let's look at what type of file babyrev is using the command `file findme`.

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/9134dbef-11cf-445b-a126-eb58b75ccb03)

It is .ELF 32-bit file so let's hop on [Ghidra](https://ghidra-sre.org/) and decompile it.

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/b3868a1e-45d3-4dc2-9248-af339d91fa2f)

When we look at the `echo` function, it says that "...  I\'m hidden, jump to me" thus implying it is hidden somewhere.
On the left side, we can see a `hiddenFunction` within the Symbol Tree section so click on it.

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/37c2cd6f-9b44-472e-b4e1-3e719c333789)

The **for loop** will XOR every item inside the bend array with the hexadecimal value of 0x12 and display it.
In this case, I created a short code to automate the process and display the output. 

```python
hex_array = [0x45, 0x41, 0x51, 0x46, 0x54, 0x20, 0x22, 0x20, 0x23, 0x69, 0x27, 0x23, 0x7F,
             0x62, 0x7E, 0x21, 0x60, 0x77, 0x64, 0x77, 0x60, 0x27, 0x21, 0x6F, 0x12]

for i in range(len(hex_array)):
    output = hex_array[i] ^ 0x12
    print(chr(output), end = '')
```

### 🏳️ Flag

Hence, the flag is `WSCTF2021{51mpl3rever53}`
