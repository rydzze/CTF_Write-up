## Crack Me

### 📚 Overview

Compressed with UPX to reduce the size, crack me if you can!

### ✨ Solution

Run `file crackme.exe` command to determine the file type and any worthwhile information.
It is stated that the file is UPX compressed. So, run `upx -d crackme.exe` command to decompress the file.

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/a1a18332-add2-48b1-b3d5-bf21d512f31a)

Next, decompile the `crackme.exe` file using [Ghidra](https://ghidra-sre.org/).

```c
int __cdecl _main(int _Argc,char **_Argv,char **_Env)

{
  int local_20;
  int local_1c;
  int local_18;
  int local_14 [3];
  
  ___main();
  _printf("Enter code: ");
  _scanf("%i-%i-%i-%i",local_14,&local_18,&local_1c,&local_20);
  if ((((local_14[0] + local_20 * 3 == 0x467c) && (local_1c * local_18 * 3 == 0x4ef3ae)) &&
      (local_14[0] == 0x3f2)) && (local_1c * 0xc0d3 + local_20 == 0x3cbbd6c)) {
    _printf("Correct code! The flag is WSCTF2021{%i-%i-%i-%i}\n",0x3f2,local_18,local_1c,local_20);
  }
  else {
    _puts("Wrong code..");
  }
  return 0;
}
```

In short, the programme will ask for a code and then it will go through four conditional statements;
1. local_14[0] + local_20 * 3 == 0x467c
2. local_1c * local_18 * 3 == 0x4ef3ae
3. local_14[0] == 0x3f2
4. local_1c * 0xc0d3 + local_20 == 0x3cbbd6c

You may solve this question with simple math skills or we can create a code to solve it automatically for us.

```python
#!/usr/bin/env python3
from z3 import *
s = Solver()
F = [BitVec(i, 16) for i in range(4)]


s.add(F[0] == 0x3f2)
s.add(F[0] + F[3] * 3 == 0x467c)
s.add(F[2] * F[1] * 3 == 0x4ef3ae)
s.add(F[2] * 0xc0d3 + F[3] == 0x3cbbd6c)

code = ""
if s.check() == sat:
    m = s.model()
    for i in range(4):
        code += f'{str(m[F[i]].as_long())}-'

print(f"Code: {code[:-1]}")
```

### 🏳️ Flag

Hence, the flag is `WSCTF2021{1010-1337-1290-5678}`
