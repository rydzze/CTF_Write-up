givenFlag = "picoCTF{w1{1wq8/7376j.:}"

print("Real flag is : ", end='')

for i in range(23):
    if i < 8:
        print(givenFlag[i], end='')
    elif i < 23:
        if i & 1 == 0:
            print(chr(ord(givenFlag[i]) - 5), end='')
        else:
            print(chr(ord(givenFlag[i]) + 2), end='')

print('}', end='')