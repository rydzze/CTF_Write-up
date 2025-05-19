flag = "SHCTF24{"
obfs_flag = "bcb4ce08a3/6317b67`d8`d58e6e1e`b"

for i in range(len(obfs_flag)):
    flag += chr(ord(obfs_flag[i]) + 1)
    
print(flag + '}')

# SHCTF24{cdc5df19b407428c78ae9ae69f7f2fac}