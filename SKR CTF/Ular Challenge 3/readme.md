## Ular Challenge 3

### 📚 Overview

Now is the 3rd challenge! Many of you love XOR right? Now is time to show off XOR skills!

### 🤔 Hint 

> _"What happen when we XOR two same numbers? Search for XOR laws to understand more"_

### ✨ Solution

Let's break down the source code first.

```python
#!/usr/bin/env python3
import sys

S1=[0, 7, 2, 1, 4, 6, 3, 5]
S2=[3, 5, 7, 4, 2, 0, 1, 6]

p=input("Enter passcode: ").encode()

if len(p)==16:
	p1,p2=p[0:8],p[8:16]
	p=[p1[s] for s in S1]
	if all([p[0]^0x1337==4967,
			p[0]^p[1]==30,
			p[1]^p[2]^p[0]==74,
			p[3]^p[4]^p[5]==48,
			p[4]^p[5]==7,
			p[4]^p[6]^p[7]==111,
			p[7]^p[4]^p[5]==55,
			p[7]^p[6]==7]):
		p=[p2[s] for s in S2]
		if all([p[1]^p[3]==68,
				p[3]^p[7]^p[1]==54,
				p[7]^p[5]^p[2]==17,
				p[5]^p[2]^p[6]==71,
				p[6]^p[0]^p[4]==68,
				p[4]^p[3]^p[0]==23,
				p[1]^p[3]^p[5]==117,
				p[1]^p[2]^p[5]==80,
				p[0]^p[2]^p[3]==21]):
			print("Correct passcode! Flag is SKR{%s}"%bytes(p1+p2).decode())
			sys.exit()

print("Wrong passcode!")
```

1. The code will ask the user to enter the passcode and then it will encode the passcode.
2. The passcode will be split in half and stored in `p1` and 'p2' respectively.
3. `p1` will be arranged according to `S1` based on their index entry.
   
```python
before = ['a', 'b', 'c']
S1 = [2, 0, 1]
after = [before[i] for i in S1]
#after = ['c', 'a', 'b']
```

4. Local variable `p` will stored `p1` and then undergoes checking through XOR.
5. Repeat steps 3 and 4 with `p2` and `S2`
6. If the passcode is correct, it will decode the passcode back and display the flag.

So, it's ~morbin'~ XOR time :D! You may refer to this [link](https://cs.stackexchange.com/questions/95318/easiest-way-to-find-y-in-x-text-xor-y-z-with-given-x-text-and-z).

```python
p=[p1[s] for s in S1]
	if all([p[0]^4919==4967,    #p[0] = 80
			p[0]^p[1]==30,          #p[1] = 78
			p[1]^p[2]^p[0]==74,     #p[2] = 84
			p[3]^p[4]^p[5]==48,     #p[3] = 55
			p[4]^p[5]==7,           #p[4] = 104
			p[4]^p[6]^p[7]==111,    #p[5] = 111
			p[7]^p[4]^p[5]==55,     #p[6] = 55
			p[7]^p[6]==7]):         #p[7] = 48

p=[p2[s] for s in S2]
  if all([p[1]^p[3]==68,      #p[0] = 48
      p[3]^p[7]^p[1]==54,     #p[1] = 51
      p[7]^p[5]^p[2]==17,     #p[2] = 82
      p[5]^p[2]^p[6]==71,     #p[3] = 119
      p[6]^p[0]^p[4]==68,     #p[4] = 80
      p[4]^p[3]^p[0]==23,     #p[5] = 49
      p[1]^p[3]^p[5]==117,    #p[6] = 36
      p[1]^p[2]^p[5]==80,     #p[7] = 114
      p[0]^p[2]^p[3]==21]):
```
Next, arrange the array back to normal.

```python
newp1 = [80, 78, 84, 55, 104, 111, 55, 48]
newp2 = [48, 51, 82, 119, 80, 49, 36, 114]

S1=[0, 7, 2, 1, 4, 6, 3, 5]
S2=[3, 5, 7, 4, 2, 0, 1, 6]

orip1 = [80, 55, 84, 55, 104, 48, 111, 78]
orip2 = [49, 36, 80, 48, 119, 51, 114, 82]
print("Flag = SKR{%s}"%bytes(orip1+orip2).decode())
#Flag is SKR{P7T7h0oN1$P0w3rR}
```


### 🏳️ Flag

Hence, the flag is `SKR{P7T7h0oN1$P0w3rR}` 
