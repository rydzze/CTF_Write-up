# [Rev] Stones

## 📚 Overview

> *"When Thanos snapped his fingers, half of the flag was blipped. We need the Avengers to retrieve the other half. There's no flag in the movie, but there is a slash flag on the server (Please do not perform any brute forcing, enumeration, or scanning. Not useful nor needed)"*

> *"Author: KD_Kasturi"*

## ✨ Walkthrough

Given .EXE file written in Python and since Python is a *hybrid programming language*, we can retrieve back the original source code :D.

### 1. Converting Python .EXE into Python bytecode .PYC 

Utilise the tool [PyInstaller Extractor](https://github.com/extremecoders-re/pyinstxtractor) to convert the executable file into the bytecode. 

### 2. Converting Python bytecode .PYC into Python source code .PY

Use the online web tool [PyLingual](https://pylingual.io/) to retrieve the source code.

```python
# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: CHAL-stones.py
# Bytecode version: 3.10.0rc2 (3439)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import requests
from datetime import datetime
from urllib.request import urlopen
from datetime import datetime

server_url = 'http://3.142.133.106:8000/'
current_time = urlopen('http://just-the-time.appspot.com/')
current_time = current_time.read().strip()
current_time = current_time.decode('utf-8')
current_date = current_time.split(' ')[0]
local_date = datetime.now().strftime('%Y-%m-%d')

if current_date == local_date:
    print("We're gonna need a really big brain; bigger than his?")

first_flag = 'WGMY{1d2993'
user_date = current_date
params = {'first_flag': first_flag, 'date': user_date}
response = requests.get(server_url, params=params)

if response.status_code == 200:
    print(response.json()['flag'])
else:
    print(response.json()['error'])
```

Based on the *given hint* within the challenge description, it is stated that '*there is a slash flag on the server*' so what we could do is to use `curl http://3.142.133.106:8000/flag` in command prompt. After the curl, we will receive an output `{"Upload Date":"https://youtu.be/V0zJb2K4Yi8?si=xUTuXD3ppkJpU2Nw&t=75"}`.

Use the upload date of the video, which is `2022-07-25`, inside the script to obtain the flag from the server.

*Sorry for the short write-up lol, FYP hits me hard*.

## ⚙ Script

```python
import requests
from urllib.request import urlopen

server_url = 'http://<IP_ADDR>:8000/'
first_flag = 'WGMY{1d2993'
date = '2022-07-25'

params = {'first_flag': first_flag, 'date': date}
response = requests.get(server_url, params=params)

if response.status_code == 200:
    print(response.json()['flag'])
else:
    print(response.json()['error'])
```

## 🏳️ Flag

`WGMY{1d2993fc6327746830cd374debcb98f5}`