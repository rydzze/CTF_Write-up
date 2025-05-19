# [Rev] sl_eep

## ✨ Walkthrough

Given binary is an ELF so lets disassemble it using [Ghidra](https://ghidra-sre.org/) and head to `checker` function.

It looks quite *confusing* at first glance so lets do some *cleaning* :D.

```c
undefined4 checker(char *flag)
{
  char underscrore;
  int cmp_string;
  size_t flag_len;
  long i;
  undefined4 check_result;
  uint check3 [8];
  uint check2 [8];
  uint check1 [22];
  
  check1[0] = 0x50a;
  check1[1] = 0x543;
  check1[2] = 0x54a;
  check1[3] = 0x54c;
  check1[4] = 0x55f;
  check1[5] = 0x558;
  check1[6] = 0x55a;
  check1[7] = 0x502;
  check1[8] = 0x55f;
  check1[9] = 0x541;
  check1[10] = 0x555;
  check1[0xb] = 0x558;
  check1[0xc] = 0x55a;
  check1[0xd] = 0x508;
  check1[0xe] = 0x556;
  check1[0xf] = 0x557;
  check1[0x10] = 0x542;
  check1[0x11] = 0x554;
  check1[0x12] = 0x50a;
  check1[0x13] = 0x54e;
  check2[0] = 0x54;
  check2[1] = 0x42;
  check2[2] = 0x45;
  check2[3] = 0x43;
  check2[4] = 0x5e;
  check2[5] = 0x59;
  check3[0] = 0x2b;
  check3[1] = 0x2d;
  check3[2] = 0x3e;
  check3[3] = 0x36;
  check3[4] = 0x31;
  flag_len = strlen(flag); 
  check_result = 0;

  // Check if the flag's length is 0x30 (48 chars) and underscores' indices in flag
  if ((((flag_len == 0x30) && (underscrore = flag[0x19], underscrore == flag[0x20])) && (underscrore == flag[0x26]))
     && (flag[0x26] == flag[0x29])) {
    if ((flag[0x2b] == flag[0x29]) && (underscrore == '_')) {

      i = 5;
      check_result = 1;

      // Part 1 checking !!!
      do {
        if (((int)flag[i] ^ 0x53b) != check1[i - 5]) {
          check_result = 0;
        }
        i = i + 1;
      } while (i != 0x19);
      
      // Part 2 checking !!!
      i = 0x1a;
      do {
        if ((int)(char)(flag[i] ^ 0x37) != check2[i - 0x1a]) {
          printf("failed second check    %c\n",(ulong)(uint)(int)flag[i]);
          check_result = 0;
        }
        i = i + 1;
      } while (i != 0x20);

      // Part 3 checking !!!
      i = 0x21;
      do {
        if (((int)flag[i] ^ 0x5f) != check3[i - 0x21]) {
          check_result = 0;
        }
        i = i + 1;
      } while (i != 0x26);

      // Part 4 checking !!!
      if (flag[0x27] != 'a') {
        check_result = 0;
      }
      if (flag[0x28] != 't') {
        check_result = 0;
      }

      // Checking for start and end !!!
      cmp_string = strncmp(flag + 0x11,"3/4}",4);
      if (cmp_string == 0) {
        cmp_string = strncmp(flag,"flag{",5);
        if ((cmp_string == 0) && (flag[0x2a] == '9')) {
          check_result = 0;
          
          // CORRECT FLAG !!!  
        }
      }
    }
    else {
      check_result = 0;
    }
  }
  return check_result;
}
```

I tried to use `z3-solver` but somehow it didn't worked lmao so I just do it manually *sobsob*. Anyway, here is the script.

## ⚙ Script

```py
head = 'flag{'
tail = '3/4}'

enc1 = [0x50a, 0x543, 0x54a, 0x54c, 0x55f, 0x558, 0x55a, 0x502, 0x55f, 0x541, 0x555, 0x558, 0x55a, 0x508, 0x556, 0x557, 0x542, 0x554, 0x50a, 0x54e]
enc2 = [0x54, 0x42, 0x45, 0x43, 0x5e, 0x59]
enc3 = [0x2b, 0x2d, 0x3e, 0x36, 0x31]

part1 = ''.join(chr(enc1[i] ^ 0x53b) for i in range(len(enc1))) + '_'
part2 = ''.join(chr(enc2[i] ^ 0x37) for i in range(len(enc2))) + '_'
part3 = ''.join(chr(enc3[i] ^ 0x5f) for i in range(len(enc3))) + '_'
part4 = 'at_9_'

flag = head + part1 + part2 + part3 + part4 + tail
print(flag)
```

## 🏳️ Flag

`flag{1xqwdca9dznca3mlyo1u_curtin_train_at_9_3/4}`