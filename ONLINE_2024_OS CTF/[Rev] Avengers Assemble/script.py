from z3 import *
s = Solver()
F = [BitVec(i, 32) for i in range(3)]

s.add(F[1] == 0x6f56df8d)
s.add(F[0] < 0x6f56df65)
s.add(F[0] + F[1] == 0xdeadbeef)
s.add(F[1] ^ F[2] == 2103609845)

flag = ""
if s.check() == sat:
    m = s.model()
    for i in range(3):
        flag += f'{str(m[F[i]].as_long())}_'

print('Flag: OSCTF{' + flag[:-1] + '}')