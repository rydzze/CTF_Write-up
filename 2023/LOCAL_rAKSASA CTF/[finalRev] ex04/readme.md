## ex04

### 📚 Overview

Decompile the `ex04.exe` file using [IDA tool](https://hex-rays.com/ida-free/) and look into `DialogFunc` function.

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/3fb730bd-79f7-40f1-ab78-41c70ff1c871)
 
The programme will ask for user input and then it will go through lots of mathematical and logical operations.

```c
String = 0;
sub_401468(v13, 0, 99);
GetDlgItemTextA(hDlg, 1000, &String, 90);
flag = sub_401358(&String, v11, 10);
encFlag = (__ROR4__(((flag ^ 0xB20083FF) >> 9) - 0xD1507BA + ((((flag ^ 0xB20083FF) >> 9) - 0xD1507BA) ^ 0xCB89034) + 0xCB89034, 7) >> 1) ^ 0x8E67212B;
if ( encFlag == 0xF298DC9E ){
  SetDlgItemTextA(hDlg, 1001, "Correct!!");
  return nullsub_1((unsigned int)&encFlag ^ v14);
}
SetDlgItemTextA(hDlg, 1001, "Wrong!!");
```

```nasm
push    eax
call    sub_401358
xor     eax, 0B20083FFh
shr     eax, 9
sub     eax, 0D1507BAh
mov     ecx, eax
xor     ecx, 0CB89034h
mov     edx, ecx
xor     edx, eax
add     edx, ecx
add     edx, eax
add     esp, 0Ch
mov     [esp+74h+encFlag], edx
mov     eax, [esp+74h+encFlag]
ror     eax, 7
shr     eax, 1
mov     ecx, 8E67212Bh
xor     eax, ecx
mov     [esp+74h+encFlag], eax
cmp     [esp+74h+encFlag], 0F298DC9Eh
```

### ✨ Solution

In order to find the correct input which is our flag, we can use [Z3 Theorem Power](https://github.com/Z3Prover/z3) to solve the operations automatically by providing
it with constraints from the source code. Let's start our operations by copying it from the decompiled source code from the bottom to the top.

```python
from z3 import *

mask = 0xFFFFFFFF
s = Solver()
F = [BitVec(i, 32) for i in range(9)]

s.add(F[0] == 0xF298DC9E)
s.add(F[1] ^ 0x8E67212B == F[0])
#logical shift left by 1 bit
s.add(F[2] == (F[1] << 1) & mask)
#bitwise left rotate by 7 bits
s.add(F[3] == (F[2] << 7) | (LShR(F[2], 32 - 7)))
#0xCB89034 + ECX + newEAX
s.add(F[3] == (0xCB89034 + F[5] + F[4]) & mask)
#ECX = newEAX ^ 0xCB89034
s.add(F[5] == (F[4] ^ 0xCB89034))
#newEAX = EAX - 0xD1507BA
s.add(F[4] == (F[6] - 0xD1507BA) & mask)
#bitwise left rotate by 9 bits
s.add(F[7] == (F[6] << 9) & mask)
#flag
s.add(F[8] == F[7] ^ 0xB20083FF)

if s.check() == sat:
    sol = s.model()
    for i in range(9):
        print("F" + str(i) + " " + hex(int(str(sol[F[i]]))).upper()[2:])
else:
    print("Error")
```

Thus, we will get `flag = F[8] == 4A40BFF`. However, our input was still wrong despite our calculation being correct so I decided to debug it using IDA.
I found that the programme will accept our input as a decimal number and convert it into a hexadecimal number. So, `F[8] == 77859839`.

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/27abd69c-4c9a-4c08-9151-4c888024be0e)

### 🏳️ Flag

Hence, the flag is `77859839`.
