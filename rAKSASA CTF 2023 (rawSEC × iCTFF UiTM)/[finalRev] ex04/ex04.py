from z3 import *

mask = 0xFFFFFFFF
s = Solver()
F = [BitVec(i, 32) for i in range(9)]

s.add(F[0] == 0xF298DC9E)
s.add(F[1] ^ 0x8E67212B == F[0])
s.add(F[2] == (F[1] << 1) & mask)
s.add(F[3] == (F[2] << 7) | (LShR(F[2], 32 - 7)))
s.add(F[3] == (0xCB89034 + F[5] + F[4]) & mask)
s.add(F[5] == (F[4] ^ 0xCB89034))
s.add(F[4] == (F[6] - 0xD1507BA) & mask)
s.add(F[7] == (F[6] << 9) & mask)
s.add(F[8] == F[7] ^ 0xB20083FF)

if s.check() == sat:
    sol = s.model()
    for i in range(9):
        print("F" + str(i) + " " + hex(int(str(sol[F[i]]))).upper()[2:])
else:
    print("Error")
