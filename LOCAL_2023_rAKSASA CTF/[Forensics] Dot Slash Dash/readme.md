## Dot Slash Dash

### 📚 Overview

Zheep Thou John is a soldier veteran. He left us a sound file. Will you discover what it contains?

### ✨ Solution

Download `morse.wav` and go to this [website](https://morsecode.world/international/decoder/audio-decoder-adaptive.html) to decode it.

The decoded text is `WELCOMETOWSCTF2021.HEREISTHEDOWNLOADLINKHTTPS://CONTROLC.COM/624EC7B2.THEPASWORDTOSEETHECONTENTISWSCTF2021`.

Go to the [link](https://controlc.com/624ec7b2/), insert the password `WSCTF2021`, and download the .ZIP file.

Use [fcrackzip](https://www.kali.org/tools/fcrackzip/) tool to crack the password and unzip it.
Refer to this [link](https://mattcasmith.net/2020/09/12/cracking-password-protected-zip-file-fcrackzip) for more information.

After that, we found that the flag is encoded in base32. So, find any base32 decoder online and insert the encoded flag.

### 🏳️ Flag

Hence, the flag is `WSCTF{M0RSE_C0DE_G0ES_TUNUNU}`.
