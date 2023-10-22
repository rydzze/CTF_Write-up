## ex01

### 🤔 Hint

> _"If you got 7575, you not encoded enough"_

### ✨ Solution

Run `file ex01` command and we will find that the file format is Mach-O :3.

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/f2a7e37e-ea28-4622-903f-e64f47bcfeb5)

Let's hop on [Ghidra](https://ghidra-sre.org/) to decompile the file and look at the `entry` func.

```c
undefined8 entry(void)

{
  int iVar1;
  undefined8 local_438;
  undefined8 local_430;
  undefined8 local_428;
  undefined8 local_420;
  char local_418 [1032];
  long local_10;
  
  local_10 = *(long *)PTR____stack_chk_guard_100001000;
  local_438._0_1_ = 'U';
  local_438._1_1_ = 'r';
  local_438._2_1_ = 'y';
  local_438._3_1_ = 'y';
  local_438._4_1_ = 'b';
  local_438._5_1_ = ' ';
  local_438._6_1_ = 'e';
  local_438._7_1_ = 'n';
  local_430._0_1_ = 'j';
  local_430._1_1_ = 'f';
  local_430._2_1_ = 'r';
  local_430._3_1_ = 'p';
  local_430._4_1_ = ' ';
  local_430._5_1_ = 'z';
  local_430._6_1_ = 'v';
  local_430._7_1_ = 'a';
  local_428._0_1_ = 'v';
  local_428._1_1_ = 'p';
  local_428._2_1_ = 'b';
  local_428._3_1_ = 'a';
  local_428._4_1_ = ' ';
  local_428._5_1_ = 'p';
  local_428._6_1_ = 'g';
  local_428._7_1_ = 's';
  local_420._0_1_ = ' ';
  local_420._1_1_ = '7';
  local_420._2_1_ = '5';
  local_420._3_1_ = '7';
  local_420._4_1_ = '5';
  local_420._5_1_ = '!';
  local_420._6_1_ = '\n';
  local_420._7_1_ = '\0';
  _s_to_rot13(&local_438);
  _printf("Please enter the password: ");
  _fgets(local_418,0x400,*(FILE **)PTR____stdinp_100001008);
  iVar1 = _strcmp(local_418,(char *)&local_438);
  if (iVar1 == 0) {
    _printf("Welldone\n");
  }
  else {
    _printf("Please try again\n");
  }
  if (*(long *)PTR____stack_chk_guard_100001000 == local_10) {
    return 0;
  }
                    /* WARNING: Subroutine does not return */
  ___stack_chk_fail();
}
```

In brief, the programme will call the `_s_to_rot13` function with a reference to the `local_438` variable.

```c
void _s_to_rot13(char *param_1)

{
  char cVar1;
  char *local_28;
  char *local_10;
  
  _strlen(param_1);
  local_28 = param_1;
  for (local_10 = param_1; *local_10 != '\0'; local_10 = local_10 + 1) {
    cVar1 = _ch_to_rot13((int)*local_10);
    *local_28 = cVar1;
    local_28 = local_28 + 1;
  }
  *local_28 = '\0';
  return;
}
```

Then, `_s_to_rot13` function will call the `_ch_to_rot13` function to apply the ROT13 cipher to the character
pointed to by `local_10`, and the result is stored in `cVar1`.

```c

int _ch_to_rot13(char param_1)
{
  char local_a;
  
  if ((param_1 < '0') || ('4' < param_1)) {
    if ((param_1 < '5') || ('9' < param_1)) {
      if ((param_1 < 'A') || ('M' < param_1)) {
        if ((param_1 < 'N') || ('Z' < param_1)) {
          if ((param_1 < 'a') || ('m' < param_1)) {
            local_a = param_1;
            if (('m' < param_1) && (param_1 < '{')) {
              local_a = param_1 + -0xd;
            }
          }
          else {
            local_a = param_1 + '\r';
          }
        }
        else {
          local_a = param_1 + -0xd;
        }
      }
      else {
        local_a = param_1 + '\r';
      }
    }
    else {
      local_a = param_1 + -5;
    }
  }
  else {
    local_a = param_1 + '\x05';
  }
  return (int)local_a;
}
```

To save our time, let's use [rot13.com](https://rot13.com/) to decipher the text. We will get "Hello rawsec minicon ctf 7575!".
However, we can see that 7575 remains the same so you have to know how the function actually works.

```c
if ((param_1 < '5') || ('9' < param_1)) {
  //if blablabla
}
else{
  local_a = param_1 + -5;
}
```

When `param_1` == 7 or 5, then `param_1 < '5'` and `'9' < param_1` are false so you have to subtract it by 5.
Congratulations, you got the flag.

### 🏳️ Flag

Hence, the flag is `Hello rawsec minicon ctf 2020!`
