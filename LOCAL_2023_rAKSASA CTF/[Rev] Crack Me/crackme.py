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


#   if ((((F[0] + F[3] * 3 == 0x467c) && (F[2] * F[1] * 3 == 0x4ef3ae)) &&
#       (F[0] == 0x3f2)) && (F[2] * 0xc0d3 + F[3] == 0x3cbbd6c)) {
#     _printf("Correct code! The flag is WSCTF2021{%i-%i-%i-%i}\n",0x3f2,F[1],F[2],F[3]
#            );
#   }
#   else {
#     _puts("Wrong code..");