## Magic Number

### 📚 Overview

![Magic Number](https://github.com/rydzze/CTF_Write-up/assets/86187059/067e3b6a-7a57-4e50-9bde-377a2b639376)

### ✨ Solution

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/b2743472-94cb-4a39-8058-bec567b84ab1)

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/9eb3302d-8d9c-4d9b-99bd-fffb82b54b01)

*disassemble main function using Ghidra and gdb-peda

```c
magicNum = calculateDynamicMagicNumber(0x12772,0x3039);
std::operator<<((basic_ostream *)std::cout,"Enter the magic number to get the secret message: ");
std::basic_istream<>::operator>>((basic_istream<> *)std::cin,&input);
if (magicNum == input) {
  //If our input is equal to the magic number, then it will print the flag.
}
```

So, we can insert a **breakpoint** after the `calculateDynamicMagicNumber` function is called using the command `b * main+37` and then **observe** the **accumulator register**.

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/e7e4eaec-8ee6-4d83-bbe3-64c507cf670f)

**Convert** the **hexadecimal**, 0x25ec5 into **decimal** and we get the magic number, 155333. 

### 🏳️ Flag

Hence, the flag is `gohunikl2023{w0w_U_G3t_Me}`
