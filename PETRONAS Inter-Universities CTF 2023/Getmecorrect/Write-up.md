### Getmecorrect

#### 📚 Overview

Debug `dynamic.apk` using `Android Studio` and dive deep into the source code to find the flag.

#### 🤔 Hint

> _"While Java holds the clues, the real answers may lie in the realm of native libraries."_

#### ✨ Solution

Let's start the challenge by reading `dynamic.apk` using an APK decompiler. In this case, I used `jadx-gui` in Kali Linux.

Whenever they give us an APK file, jump straight to the `MainActivity` inside /com directory.

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/77383697-0223-49b1-9516-54b4daa60cda)

It looks like the string flag was split into 4 parts and it will be combined together later on. Let's take a look at `LiveLiterals$MainActivityKt`.

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/c9f2a0ff-5bee-4106-a815-9b720628a6f7)

We have obtained parts 1, 2, and 4 of the string so we have to find where is part 3 stored. 

```Java
public final String m5402String$arg0$callloadLibrary$classCompanion$classMainActivity() {
        if (LiveLiteralKt.isLiveLiteralsEnabled()) {
            State<String> state = f52x1d7c04fd;
            if (state == null) {
                state = LiveLiteralKt.liveLiteral("String$arg-0$call-loadLibrary$class-Companion$class-MainActivity", f57String$arg0$callloadLibrary$classCompanion$classMainActivity);
                f52x1d7c04fd = state;
            }
            return state.getValue();
        }
        return f57String$arg0$callloadLibrary$classCompanion$classMainActivity;
    }
```

By looking at this function inside `LiveLiterals$MainActivityKt`, I assumed that the source code loads the library to get the string value AND not to mention that the string `f57String$arg0$callloadLibrary$classCompanion$classMainActivity` was assigned with the value "nativeFlagPart". This actually hints to us that we have to access the native library of the APK file to get part 3 of the string (This one I _'palatao'_ lol).

So, we have to debug `dynamic.apk` using an APK debugger. In this case, I used `Android Studio` in Windows. 

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/772d34d4-e7d8-4e9b-b834-260dff758ecd)

After the debugging process, I still didn't manage to open the file so I hopped on Ghidra straight away. You can find the `libdynamicflagchallenge.so` file by referring to the top ribbon in the image above (varies depending on the user).

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/f47a3c69-0385-4942-91e4-b049935b99f1)

#### 🏳️ Flag

Hence, the flag is `petgrad2023{Qu@ntum_N3xu$_C0d3br3@k3r}`
