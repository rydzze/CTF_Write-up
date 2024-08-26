# [Rev] Micro Rev

## 📚 Overview

> *"First C reverse engineering challenge :P"*

## ✨ Walkthrough

Given .ELF binary that is written in C language, the programme will asks for string argument (*which is the flag*), takes the value for **bitwise XOR operation**, and then **write the results** inside `enc.txt` file. For this challenge, we just need to reverse the operation. 

In this case, let's use [Ghidra](https://ghidra-sre.org/) to analyse the binary and navigate to the `main` and `xorMessage` functions. 

```C
undefined8 main(int param_1,undefined8 *message)

{
  undefined8 uVar1;
  void *enc_flag;
  FILE *file_stream;
  
  if (param_1 < 2) {
    fprintf(stderr,"Usage: %s <secret message>\n",*message);
    uVar1 = 1;
  }
  else {
    enc_flag = (void *)xorMessage(message[1],&key);
    file_stream = fopen("enc.txt","w");
    if (file_stream == (FILE *)0x0) {
      perror("Failed to open file for writing");
      free(enc_flag);
      uVar1 = 1;
    }
    else {
      fprintf(file_stream,"%s\n",enc_flag);
      fclose(file_stream);
      free(enc_flag);
      puts("Encrypted message saved to enc.txt");
      uVar1 = 0;
    }
  }
  return uVar1;
}
```

```C
void * xorMessage(char *message,char *key)

{
  size_t input_len;
  size_t key_len;
  void *enc_flag;
  ulong i;
  
  input_len = strlen(message);
  key_len = strlen(key);
  enc_flag = malloc(input_len + 1);
  if (enc_flag == (void *)0x0) {
    perror("Memory allocation failed");
    exit(1);
  }
  for (i = 0; i < input_len; i = i + 1) {
    *(char *)(i + (long)enc_flag) = key[i % key_len] ^ message[i];
  }
  *(undefined *)(input_len + (long)enc_flag) = 0;
  return enc_flag;
}
```

Inside `xorMessage` function, we could see the XOR operation, where `the value of message ⊕ the value of key`. That said, let's **reverse the operation** by doing XOR operation between `enc_flag` and `key` using Python ... Retrieve the encrypted flag string from `enc.txt` directly using Windows' Notepad and then convert the ASCII to Hex using [online converter](https://www.rapidtables.com/convert/number/ascii-to-hex.html), the `key` can be retrieved from the binary itself.

## ⚙ Solution

```python
enc_flag = [0x76, 0x52, 0x25, 0xd0, 0x36, 0x69, 0x67, 0x1c, 0x201a, 0x14, 0x4d, 0x4e, 0x16, 0x2030, 0x7, 0x7e, 0x66, 0x10, 0x8f, 0x1, 0x47, 0x4e, 0x13, 0x17d, 0x14, 0x4d, 0x69, 0x2a, 0x201c, 0x3, 0x54, 0x74, 0x7, 0x2019, 0x3, 0x60, 0x55, 0x2d, 0xb1, 0x1b]
key = [0x22, 0x11, 0x75, 0xe1, 0x66, 0x12, 0x0a, 0x75, 0xe1, 0x66]
    
flag = ''.join(chr(enc_flag[i] ^ key[i % len(key)]) for i in range(len(enc_flag)))

print(flag)
```

Run the code, and then change some of the non-ASCII character *manually*. 

## 🏳️ Flag

`TCP1P{micro_challenge_for_c_reverser_XP}`