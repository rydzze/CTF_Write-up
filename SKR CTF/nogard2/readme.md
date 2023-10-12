## nogard2

### 📚 Overview

Ghidra reversing challenge 2!
We all love XORing!

### 🤔 Hint 

> _"How do we reverse the XOR process using the 1st key?"_

### ✨ Solution

Open the file using [IDA tool](https://hex-rays.com/ida-free/), decompile it and then press F5 to look at the source code.

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/b1a8a21a-aee9-4617-8b80-a69da0f57494)

If we look at the if-else statement inside the for loop, there are two conditional statements that we have to follow if we want the correct key;
- `part1[i] should be equal to v5[i], which is the first key.`
- `v5[i] ^ v6[i] should be equal to enc[i] (First key XOR w/ Second key).`

Double left-click _~lol~_ on the `part1` variable and eventually, it will lead us to the hex values of `part1` and `enc`.

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/89355f9b-0b2a-4677-85cb-1adc449acfcb)

Convert the hex values of `part1` and `enc` to ASCII characters, then XOR `part1` with `enc` to get `part2` by using [CyberChef](https://gchq.github.io/CyberChef/#recipe=XOR(%7B'option':'UTF8','string':''%7D,'Standard',false))

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/b382f64a-e66f-4307-9f53-e095b72ebc97)

### 🏳️ Flag

Hence, the flag is `SKR{XoRF0rL1f3!}` 
