### Reverseme

#### Overview

Disassemble `myapps.apk` using `apktool` and dive deep into the source code to find the flag.

#### Solution

Let's start the challenge by reading `myapps.apk` using the APK decompiler. In this case, I used `jadx-gui` in Kali Linux. Whenever they give us an APK file, jump straight to the `MainActivity` inside /com directory.

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/79c780b6-5b33-4290-9a5a-e17d576691e6)

It looks like there is a function that is going to get the string flag and hence, we can say that the string flag is stored inside the APK file.

Next, we disassemble the APK file using a command, `apktool d myapps.apk`. After that, go to ~/myapps/res/values and use this command, `strings *.xml | grep -i flag` to find the flag.

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/855ffcd0-9f42-4806-bda9-5eb321d94dce)

#### Flag

Hence, the flag is `{PETGRAD2023}_S1mPl3Fl4g` (Accepted due to the author's error)  
