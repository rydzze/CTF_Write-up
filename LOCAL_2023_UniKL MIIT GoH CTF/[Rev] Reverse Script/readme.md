## Reverse Script

### 📚 Overview

![Reverse Script](https://github.com/rydzze/CTF_Write-up/assets/86187059/d8cdd562-f820-47b8-b7a2-d4c9d1decf8a)

### ✨ Solution

```python
arg444 = arg132()           # open file, read flag 
arg432 = arg232()           # ask for password from user
arg133(arg432)              # check if passwords are correct, else exit
arg112()                    # "Welcome back, your flag is ..."
arg423 = arg111(arg444)     # decode flag
print(arg423)               # flag
```

I'm gonna make it short, the programme ask for two passwords and if it is correct, then it will print flag.
The **password** is equal to `arg432` (inside `func arg133`) which is **GodziLl@VSK1ngGh1d0r4H**. For the input, it will join 1st pass with 2nd pass.
So, it doesn't matter what your input is, as long as 1st pass join with 2nd pass is **GodziLl@VSK1ngGh1d0r4H**, you good.

*_SHORTCUT: just comment some functions and it will print the flag straightaway_

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/69006028-5d28-40d8-b1a9-dc4f78b79588)

### 🏳️ Flag

Hence, the flag is `gohunikl2023{m0n4rch.s3cr37}`
