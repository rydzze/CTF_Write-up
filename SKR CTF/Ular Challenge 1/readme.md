## Ular Challenge 1

### 📚 Overview

Enter the correct passcode to get the flag, easy right?

### 🤔 Hint 

> _"It is not as complicated as it seems.."_

### ✨ Solution

```python
print("}s%{RKS si galF !edocssap tcerroC"[::-1] % p
      if len(p) == 9
      and p[1337^1337] == 'D'
      and p[1**1337] == '3'
      and p[len('2'*2)] == '4'
      and p[3] == p[len('')]
      and p[len('skrr')] == '-'
      and p[5] == 'B'
      and p[(len('6'*6)-5)*6] == p[1<<1337>>1337]
      and p[int(p[6])+4] == p[len(p)-3]
      and p[len(p[1:])] == 'F'
      
      else " ! e d o c s s a p   g n o r W"[::-1][::2])
```

The passcode needs to meet all these criteria in order to display the flag. First, let's clean the if-else statement. 

```python
p[0] == 'D'
#1337 XOR 1337 is 0 
p[1] == '3'
#1 power of 1337 is 1
p[2] == '4'
#multiply a char by 2 thus len is 2
p[3] == p[0]
#len of '' is 0
p[4] == '-'
#len of 'skkr' is 4
p[5] == 'B'
p[6] == p[1]
#simple math :)
#shift left and right by 1337 bits, it will cancel each other
p[7] == p[6]
#simple math xD
#9 minus 3
p[8] == 'F'
#returns the len(p) starting from the 2nd element to the end
```

### 🏳️ Flag

Hence, the flag is `SKR{D34D_B33F}` 
