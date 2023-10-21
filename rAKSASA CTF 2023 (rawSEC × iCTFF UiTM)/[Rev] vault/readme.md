## Vault

### 📚 Overview

Crack this vault open.

### ✨ Solution

Decompile the `vault.apk` by using [jadx-gui](https://github.com/skylot/jadx) and then go to /vault.apk/Source code/my.trg.vault/MainActivity.

```java
new String[]{"r", "a", "w", "s", "e", "c"};
new String[]{"c", "s", "m"};
String[] strArr = {"WSCTF2021{", "}"};

TextView textView = (TextView) findViewById(R.id.textView3);
String stringExtra = getIntent().getStringExtra(MainActivity.PWD);

if(stringExtra.trim().equals(10 + new String[]{"w", "a", "r", "g", "a", "m", "e", "s", "m", "y"}[1] + "312nasikakwok")){
    textView.setText("\n" + strArr[0] + generate(stringExtra) + strArr[1]);
}
else{
    textView.setText("Please go back and try again.");
}
```

The .APK file will display the flag if our input is equal to what it is inside the if-statement. So, the passcode is "10a312nasikakwok".
Install the .APK file and insert the passcode thus it will display the flag.

### 🏳️ Flag

Hence, the flag is `WSCTF2021{9aef6076925548c4ee1d3ecd24ff70f2}`
