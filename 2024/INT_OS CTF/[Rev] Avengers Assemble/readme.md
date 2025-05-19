# [Rev] Avenger Assemble

## 📚 Overview

> *"The Avengers have assembled but for what? To solve this!? Why call Avengers for such a simple thing, when you can solve it yourself"*

## 🔎 *Reconnaissance*

Reversing Assembly 101, the programme asks for three inputs and it will do checking if it is valid or not soo let's *cut to the chase*.

The code will store three inputs in three locations where;

- inp1 : `[ebp-0x4]`
- inp2 : `[ebp-0xc]`
- inp2 : `[ebp-0x14]`

However, there will be some constraints to validate whether the input (*our flag in this context*) is correct or not ...

1. `inp1 + inp2 == 0xdeadbeef`

```asm
mov ebx, DWORD[ebp-0xc]
add ebx, DWORD[ebp-0x4]
cmp ebx, 0xdeadbeef
jne N ; if not equal, jump to "Not Correct"
```

2. `inp1 < 0x6f56df65`

```asm
cmp DWORD[ebp-0x4], 0x6f56df65
jg N ; if greater, jump to "Not Correct"
```

3. `inp2 == 0x6f56df8d`

```asm
cmp DWORD[ebp-0xc], 0x6f56df8d
jg N ; if greater, jump to "Not Correct"
cmp DWORD[ebp-0xc], 0x6f56df8d
jl N ; if lower, jump to "Not Correct"
```

4. `inp2 ⊕ inp3 == 2103609845`

```asm
mov ecx, DWORD[ebp-0x14]
mov ebx, DWORD[ebp-0xc]
xor ecx, ebx
cmp ecx, 2103609845
jne N ; if not equal, jump to "Not Correct"
jmp O ; otherwise, jump to "Correct"
```

## ✨ Solution

> *"With this treasure, I summon [z3-solver](https://github.com/Z3Prover/z3)!"*

We can automate the process to solve it using a Python package, that's all ;).

## 🏳️ Flag

`OSCTF{1867964258_1867964301_305419896}`