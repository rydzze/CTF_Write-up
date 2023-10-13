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

[`lambda` function](https://www.w3schools.com/python/python_lambda.asp) is a small anonymous function (it works like a function in math, f(x) = x + 1) ...
On the left-hand side, we have the function name, right after the lambda is the arguments, and the math operation it executed is located after the colon.
Now, let the math begin :D!

```python
if(len(p)==8):
	if(a(p[0],p[1])==c(52) and b(p[1],p[0])==-2):
        #p[0]+p[1] = 104         p[1]-p[0] = -2
        #p[1]+2+p[1] = 104  <--       p[0] = p[1]+2
        #     2*p[1] = 102    -->      p[0] = 51+2
        #       p[1] = 51   --^       p[0] = 53
		if(a(p[2],p[3])-b(p[3],p[2])==a(int(chr(p[0])+chr(p[1])),45) and c(p[2])+c(p[3])==b(-1141,-1337)):
            #p[2]+p[3]-(p[3]-p[2]) = 53+45             2*p[2]+2*p[3] = -1141+1337
            #               2*p[2] = 98       --->            2*p[3] = 98
            #                 p[2] = 49    ---^                 p[3] = 49
			if(a(c(p[4]),c(p[5]))==c(108) and b(c(p[5]),c(p[4]))==-12):
                #2*p[4]+2*p[5] = 2*108          2*p[5]-2*p[4] = -12
                #    p[4]+p[5] = 108                p[5]-p[4] = -6
                #     2*p[5]+6 = 108       <--           p[4] = p[5]+6
                #         p[5] = 51        -->           p[4] = 57
				if(b(a(p[6],p[7]),b(p[6],p[7]))==108 and b(c(b(p[7],p[6])),a(p[7],p[6]))==-111):
                    #    p[6]+p[7]-(p[6]-p[7]) = 108     2*(p[7]-p[6])-(p[7]+p[6]) == -111
                    #                   2*p[7] = 108       2*p[7]-2*p[6]-p[7]-p[6] = -111
                    #                     p[7] = 54    -->             p[7]-3*p[6] = -111
                    #                                                      -3*p[6] = -165
                    #                                                         p[6] = 55
					print("Correct passcode! Flag is SKR{%s}"%bytes(p).decode())
```

### 🏳️ Flag

Hence, the flag is `SKR{53119376}` 
