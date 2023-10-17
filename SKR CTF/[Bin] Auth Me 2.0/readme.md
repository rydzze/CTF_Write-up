## Auth Me 2.0

### 📚 Overview

Due to some issues in version 1. We have upgraded Auth Me to 2.0, now no one can log in as admin =). You can find the program and source code in our web shell.
Tips: Press `ctrl + shift + @` to enter a null character.

### 🤔 Hint 

> _"In C programming, it stops reading when it sees ____ terminating character?"_

### ✨ Solution

To print the flag, we have to assign both `username` and `password` variables with “**admin**”, but we have to pass the first if-else statement.

So, let’s copy and compile the source code, and run it locally at first to see how the programme works (make sure to create a flag.txt file before executing the programme).

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/20d4e6b5-d73a-4f9a-9194-2e3e6e53ff7c)

The programme executed normally, and we got a hint that the distance between user and pass is 8. Hmmm, let’s debug this programme using `gdb-peda` to understand it deeper.

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/4ce6c2ea-09ce-4af6-8627-7e131568adc1)

So, I inserted the value for both `username` and `password` variables as previously and found that it is executing two lines of Assembly code that
“calculate the effective memory address at a specific offset from the base pointer `rbp` and store it in the `rax` register” (_thanks ChatGPT for the explanation_),
`lea rax,[rbp-0x8]` and `lea rax,[rbp-0x10]` for `username` and `password` variables respectively.

Considering the facts that user and pass are stored in 0024-0031 and 0016-0023 respectively, and the distance between user and pass is 8, we will exploit the gets function
to pass the value into the memory through buffer overflow.

```bash
$ echo -e "\x0aadmin\x00\x00\x00admin" | ./auth2
```

We can use this command line to do it, pairing `echo` with `pipeline` to pass the text when we execute the programme and `-e` option enables interpretation of backslash escapes
in the string. Starting from the end of the string, “**admin**” is the value that will be passed to the `user` variable, “**\x00\x00\x00**” acts as padding to fill the `char user[8]`
so that we can pass the second “**admin**” to the `pass` variable, and lastly “**\x0a**” is a newline character to enter the data.

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/14d1dd1e-8f21-4979-a1d9-a17b49ebae50)

### 🏳️ Flag

Hence, the flag is `SKR{C_St0p_rE4dinG_untIL_nuLL_6f3851}` 
