#!/usr/bin/env python3
import sys
a=lambda a,b:a+b
b=lambda b,c:a(b,-c)
c=lambda c:b(c,-c)

p=list(input("Enter passcode: ").encode())

if(len(p)==8):
	if(a(p[0],p[1])==c(52) and b(p[1],p[0])==-2):
		if(a(p[2],p[3])-b(p[3],p[2])==a(int(chr(p[0])+chr(p[1])),45) and c(p[2])+c(p[3])==b(-1141,-1337)):
			if(a(c(p[4]),c(p[5]))==c(108) and b(c(p[5]),c(p[4]))==-12):
				if(b(a(p[6],p[7]),b(p[6],p[7]))==108 and b(c(b(p[7],p[6])),a(p[7],p[6]))==-111):
					print("Correct passcode! Flag is SKR{%s}"%bytes(p).decode())
					sys.exit()

print("Wrong passcode!")