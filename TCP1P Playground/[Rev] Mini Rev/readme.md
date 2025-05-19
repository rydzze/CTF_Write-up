# [Rev] Mini Rev

## 📚 Overview

> *"First C++ reverse engineering challenge :P"*

## ✨ Walkthrough

Given .ELF binary that is written in C++ language, the programme is *quite similar* to the another challenge, **Micro Rev**. For this challenge, we just need to reverse the operation. 

In this case, let's use [Ghidra](https://ghidra-sre.org/) to analyse the binary and navigate to the `xorMessage` function.

```cpp
basic_string * xorMessage(basic_string *enc_flag,basic_string *input)

{
  byte *enc_message;
  ulong input_len;
  ulong key;
  int i;
  byte input_byte;
  byte key_byte;
  
  std::__cxx11::basic_string<>::basic_string(enc_flag);
  std::__cxx11::basic_string<>::length();
  i = 0;
  while( true ) {
    input_len = std::__cxx11::basic_string<>::length();
    if (input_len <= (ulong)(long)i) break;
    enc_message = (byte *)std::__cxx11::basic_string<>::operator[]((ulong)input);
    input_byte = *enc_message;
    enc_message = (byte *)std::__cxx11::basic_string<>::operator[](key);
    key_byte = *enc_message;
    enc_message = (byte *)std::__cxx11::basic_string<>::operator[]((ulong)enc_flag);
    *enc_message = input_byte ^ key_byte;
    i = i + 1;
  }
  return enc_flag;
}
```

Inside `xorMessage` function, we could see the XOR operation, where `the value of input ⊕ the value of key`. That said, let's **reverse the operation** by doing XOR operation between `enc_flag` and `key` using Python ... Retrieve the hex value of encrypted flag from `enc.txt` using HxD Hex Editor (*or just read the content directly using code*), and the `key` can be retrieved from the binary itself.

## ⚙ Solution

```python
enc_flag = [0x22, 0x61, 0xC9, 0xC3, 0x41, 0x1C, 0x93, 0x0F, 0x18, 0x4B, 0xC6, 0x80, 0x74, 0x11, 0xA1, 0x00, 0x19, 0x50, 0xC6, 0x9F, 0x78, 0x09, 0x97, 0x39, 0x15, 0x4A, 0xF8, 0x9E, 0x7D, 0x02, 0x90, 0x01, 0x13, 0x7D, 0xC1, 0xB6, 0x6C]
key = [0x76, 0x22, 0x99, 0xf2, 0x11, 0x67, 0xfe, 0x66]
    
flag = ''.join(chr(enc_flag[i] ^ key[i % len(key)]) for i in range(len(enc_flag)))

print(flag)
```

## 🏳️ Flag

`TCP1P{mini_rev_for_mini_challenge_XD}`