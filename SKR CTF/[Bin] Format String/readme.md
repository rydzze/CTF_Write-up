## Format String

### 📚 Overview

Format string is one of the common vuln in Binary, see can you leak the flag out of it. You can find the program and source code in our web shell.

### 🤔 Hint 

> _"What happens when u put ur name as %x ?"_
> _"The flag is put somewhere at the stack, how to leak it?"_
> _"Hope this [video](https://www.youtube.com/watch?v=rkoP2mtwFNI) helps"_

### ✨ Solution

When we look at the source code, we can see that the gets function is vulnerable to format string attacks. So, what we can do is pass it a string `%x` to read the stack.
We know that the header of the flag, `SKR{` is `534b527b` in hex. Thus, it should be easier for us to locate where is the flag in the stack.

In this case, I copied and compiled the source code, and ran it locally first with a fake flag, `CTF{th1s_1s_f4k3_f14g_sorry_:D}` (`CTF{` is `4354467b` in hex) stored in flag.txt.

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/e4ea1788-c926-4207-a1cb-b04e1b54d89d)

After a long sequence of `0x7025207025207025` and etc., we found a hexadecimal number of `0x733168747b465443` and when we convert it into ASCII text string, the result is
`s1ht{FTC` which is our flag stored in little-endian format. Now we know the location (offset) of the flag starting at `%14` in the stack, we can print the actual flag in the server.

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/39a448e1-49a5-4cb8-b68f-7c8ad844b649)

Rearrange it in big-endian format and convert it into ASCII text string. Congratulation! You found the flag :D 

### 🏳️ Flag

Hence, the flag is `SKR{L34k_7h3_Fl4G_fr0m_St4cK_9ca837}` 
