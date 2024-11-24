# [Rev] X 🩸

## 📚 Overview

> *"Its a windows world"*

## ✨ Walkthrough

Given .EXE file written in C++ ... The programme is a flag checker, we insert the flag and it will verify whether the flag is correct or not.

Let's analyse the programme using [IDA](https://hex-rays.com/ida-free). After that, we open up the strings subview to find something interesting and then we found a suspicious string literally at the most bottom. What I did is that I go to function that utilise the data and we found the function that responsible in validating the flag.

```cpp
__int64 flag_checker()
{
  int i; // [rsp+0h] [rbp-58h]
  unsigned __int64 flag_len; // [rsp+8h] [rbp-50h]
  char user_input[32]; // [rsp+18h] [rbp-40h] BYREF

  memset(user_input, 0, sizeof(user_input));
  flag_len = -1i64;
  do
    ++flag_len;
  while ( flag[flag_len] );
  if ( flag_len < 0x26
    || (flag[0] ^ 0x6B) != 56
    || (flag[1] ^ 0x75) != 61
    || (flag[2] ^ 0x65) != 38
    || (flag[3] ^ 0x68) != 60
    || (flag[4] ^ 0x74) != 50
    || (flag[5] ^ 0x69) != 91
    || (flag[6] ^ 0x6F) != 91
    || (flag[7] ^ 0x77) != 12
    || (flag[40] ^ 0x78) != 5 )
  {
    return 0i64;
  }
  qmemcpy(user_input, &flag[8], sizeof(user_input));
  for ( i = 0; i < 32; ++i )
  {
    if ( user_input[i] - 1 != obfs_flag[i] )
      return 0i64;
  }
  return 1i64;
}
```

From this *decompiled source code* alone, we able to understand the **flag's properties** where;
1. First 8 characters are the *prefix* format `SHCTF24{`.
2. Last character of the flag is `}`
3. Length of the flag is 41 since that last index is 40.

Lastly, there is a for-loop that will do the checking for the flag's content. Since the obfuscation process isn't really that complicated, we can reverse the process to retrieve the flag easily.

## ⚙ Script

```python
flag = "SHCTF24{"
obfs_flag = "bcb4ce08a3/6317b67`d8`d58e6e1e`b"

for i in range(len(obfs_flag)):
	flag += chr(ord(obfs_flag[i]) + 1)
    
print(flag + '}')
```

## 🏳️ Flag

`SHCTF24{cdc5df19b407428c78ae9ae69f7f2fac}`