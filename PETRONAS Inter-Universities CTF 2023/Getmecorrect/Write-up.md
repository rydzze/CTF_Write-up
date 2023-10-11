### Getmecorrect

#### Overview

Debug `dynamic.apk` using `Android Studio` and dive deep into the source code to find the flag.

#### Hint

> _"While Java holds the clues, the real answers may lie in the realm of native libraries."_

#### Solution

Let's start the challenge by reading `dynamic.apk` using an APK decompiler. In this case, I used `jadx-gui` in Kali Linux.

Whenever they give us an APK file, jump straight to the `MainActivity` inside /com directory.

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/77383697-0223-49b1-9516-54b4daa60cda)

It looks like that the string flag is splitted into 4 parts and it will be combined together later on. Let's take a look on `LiveLiterals$MainActivityKt`.

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/c9f2a0ff-5bee-4106-a815-9b720628a6f7)

We have obtained part 1, 2, and 4 of the string so we have to find where is the part 3 stored. 

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

Let's start the challenge by debugging `dynamic.apk` using an APK debugger. In this case, I used `Android Studio` in Windows.

#### Flag

Hence, the flag is `{PETGRAD2023}_S1mPl3Fl4g` (Accepted due to the author's error)  
