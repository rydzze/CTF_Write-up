## Ular Challenge 2

### 📚 Overview

Welcome to the 2nd challenge! Not so easy anymore, Hehe..

### 🤔 Hint 

> _"Don't waste your math skills!"_

### ✨ Solution

```python
a = lambda a,b : a+b
    #1st args + 2nd args
b = lambda b,c : a(b,-c)
    #1st args - 2nd args
c = lambda c   : b(c,-c)
    #args * 2 (c + -(-c))
```

[`lambda` function](https://www.w3schools.com/python/python_lambda.asp) is a small anonymous function (it works like function in math, f(x) = x + 1) ...
On the left-hand side, we have the function name, right after the lambda is the arguments, and the math operation it executed is located after the colon.   

```python

```

### 🏳️ Flag

Hence, the flag is `SKR{D34D_B33F}` 
