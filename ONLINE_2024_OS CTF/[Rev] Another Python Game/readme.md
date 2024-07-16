# [Rev] Another Python Game

## 📚 Overview

> *"You know, I love Pygame why don't you. Prove your love for Pygame by solving this challenge Note: It is necessary to keep the background.png file in the same place as the exe file so that the exe file runs properly"*

## ✨ Solution

1. We are given an `.EXE file` that is wrote in Python ... we can use [pyinstxtractor](https://github.com/extremecoders-re/pyinstxtractor) to decompile the binary.

2. After that, find the `source.pyc`, which is a Python bytecode file and then use [uncompyle6](https://pypi.org/project/uncompyle6/) to decompile the bytecode into .py file. You can find the flag inside the source code, thanks ;).

## 🏳️ Flag

`OSCTF{1_5W3ar_I_D1dn'7_BruT3f0rc3}`