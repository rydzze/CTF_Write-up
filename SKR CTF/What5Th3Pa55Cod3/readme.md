## What5Th3Pa55Cod3

### 📚 Overview

After we used Kuki's birthday to unlock a phone in his place. We found a mysecret.apk in the phone but it needs passcode to view the secret.

Note: Download the qrcode.png to scan and download using android device

### 🤔 Hint 

> _"You need a apk decompiler"_

> _"Whats the opposite of “Compile” ?"_

### ✨ Solution

Let's start the challenge by reading `mysecret.apk` using an APK decompiler. In this case, I used `jadx-gui` in Kali Linux.

After that, I jump straight to the `MainActivity` and `Main2Activity` inside /com/kukigodam.mysecret directory.

```Java
//from MainActivity
public void onTextChanged(CharSequence s, int start, int before, int count) {
    if (s.toString().equals("6666")) {
        MainActivity.this.startActivity(new Intent(MainActivity.this, Main2Activity.class));
    }
}

//from Main2Activity
public void onTextChanged(CharSequence s, int start, int before, int count) {
    if (s.toString().equals("19971025")) {
        Main2Activity.this.startActivity(new Intent(Main2Activity.this, SecretActivity.class));
    }
}
```

Now, we have obtained two strings which are "**6666**" and "**19971025**".
"**6666**" might be a passcode and "**19971025**" looks like a date of birth.
So, download the APK file first to unveil the secret.

Once you downloaded the `mysecret.apk`, you are required to insert the passcode and date of birth.
So, fill it and then, it will display the flag.

### 🏳️ Flag

Hence, the flag is `SKR{Y0U_F0UND_MY_CIGAR3TT35}` 
