# [Rev] Brute Force Frenzy

## 📚 Overview

> *"Your manager's software has locked him out again. This time, the manager has lost the original key and urgently needs your help. Can you use your technical skill to brute-force the key and save the day once more? Flag format: ihack24{correct_license_key}"*

## ✨ Walkthrough

Given an .EXE file, so let’s use [Ghidra](https://ghidra-sre.org/) to analyse the file and after that, navigate to the `check_license_key()` function.

```c
bool check_license_key(char *param_1)
{
  int enc_key;
  size_t keyLength;
  bool check;
  int i;
  int key;
  
  keyLength = strlen(param_1);
  if (keyLength == 8) {
    key = 0;
    for (i = 0; i < 8; i = i + 1) {
      enc_key = ((int)param_1[i] * (i + 1) + 0xd) % 0x61;
      key = key + enc_key;
      if (enc_key != *(int *)(&DAT_140010000 + (longlong)i * 4)) {
        return false;
      }
    }
    check = key == target_sum;
  }
  else {
    check = false;
  }
  return check;
}
```

This function will **take an input** (*license key*) from the user, **obfuscate** it, and then **compare** it with the key that has been encoded (*which can be found in DAT_140010000*). For the obfuscation process,

1. The char will be **multiplied** with (i + 1).
2. After that, **added** it with 0xD.
3. Lastly, **take the remainder** of *its* division with 0x61 (*using % operator*).

The problem is, reversing the modulo process would be troublesome because there are quite number of possible values for the character of the original key. Well, nevermind, that isn’t a problem anymore 😼.

*“With this treasure, I summon bruteforce techniques!”*. Since the length of the key is only 8 characters and the number of printable ASCII characters are not really that big, bruteforce is quite feasible in this case :D (*I mean, its also mentioned in the challenge title*).

```python
ENC_KEY = [0x5B, 0x3E, 0x42, 0x13, 0x3B, 0x33, 0x48, 0x29]
ASCII_START = 0x21
ASCII_END = 0x7e

key = ''
for i in range(len(ENC_KEY)):
    for char in range(ASCII_START, ASCII_END):
        guess = (char * (i+1) + 0xd) % 0x61 
        if guess == ENC_KEY[i]:
            key += chr(char)
            break

print("Key:", key)

# ENC_KEY – Retrieved from the binary itself.
# ASCII_START, ASCII_END – Range of printable ASCII character.

# Short pseudocode to briefly explain the process ...
# Loop through each position
# Loop through each printable ASCII character
# Obfuscate the character, and then compare. If matched, store in key variable.
```

## 🏳️ Flag

`ihack24{NI220G24}`