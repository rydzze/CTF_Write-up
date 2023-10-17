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