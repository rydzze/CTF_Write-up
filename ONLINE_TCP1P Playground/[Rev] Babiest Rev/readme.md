# [Rev] Babiest Rev

## 📚 Overview

> *"What is cross-reference anyway?"*

## ✨ Walkthrough

Given .EXE binary that is written in Golang, the programme will read the content (*which is the flag string*) from `flag.txt` file and then **validate the flag** whether it is **right or wrong**.

In this case, let's use [IDA Hex Rays](https://hex-rays.com/) to analyse the binary and navigate to the `main_main` function.

![img](../images/babiest_rev.png)

We could see that the programme will do **checking for every character** starting from the **beginning of the flag string**. That said, just scroll from top to bottom and copy the value to retrieve the flag.

## 🏳️ Flag

`TCP1P{g0_w1th_the_fl0w!}`