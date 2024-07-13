## Reverse It

### 📚 Overview

![Reverse It](https://github.com/rydzze/CTF_Write-up/assets/86187059/b4f60b5a-6355-4eb0-beca-7f1bd310d67a)

```python
my_string = "My_Strings"
my_result = ""

for i in range(0, len(my_string), 2):
    my_first_letter = ord(my_string[i]) << 8
    my_second_letter = ord(my_string[i + 1])
    my_final = chr(my_first_letter + my_second_letter)
    my_result += my_final

print(my_result)
```

### ✨ Solution

The idea behind it is pretty simple actually 🤥. The code will **take** the **string** in `my_string`, **encode** it, and then **print** it back.

Inside the for loop, the code will **shift** the **bit** in the **first character** by **8 bits to the left**, **add** it **with** the **second character** value, and store it in the `my_result`.
In short, it's gonna **store two characters** into one. 

```python
my_first_letter = 01100111   #char g
my_second_letter = 01101111  #char o

#shift 8 bits to the left in my_first_letter
my_first_letter = 0110011100000000

#add it with my_second_letter
my_final = 0110011101101111
```

So, what we can do is we can take the **first 8 bits** in the **character** using the **bitwise AND operation** and store it in the `second_char` variable.
After that, we **shift** the **bit** in the character by **8 bits to the right** and store it in the `first_char` variable.
Then, **add** `first_char` with `second_char` and **append** it to the `decoded_result` variable.
**Repeat** the process for every character in the `encoded_string` variable using for loop.

```python
encoded_string = "杯桵湩歬㈰㈳筎ㅣ敟剥癥牳ㅮ杽"
decoded_result = ""

for i in range(0, len(encoded_string)):
    my_first_letter = ord(encoded_string[i])
    second_char = chr(my_first_letter & 0xFF)
    first_char = chr((my_first_letter >> 8) & 0xFF)
    decoded_result += first_char + second_char  

print(decoded_result)
```

### 🏳️ Flag

Hence, the flag is `gohunikl2023{N1ce_Revers1ng}` 
