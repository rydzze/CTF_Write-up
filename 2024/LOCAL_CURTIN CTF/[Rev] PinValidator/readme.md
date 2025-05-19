# [Rev] PinValidator

## ✨ Walkthrough

Given file is an APK so lets decompile it using [jadx-gui](https://www.kali.org/tools/jadx/) and head to `MainActivity` class.

At first, we found a PIN, a *sus* string, and also a key.

```java
private static final String HARDCODED_PIN = "7331";
private static final String HARDCODED_STRING = "^\"u}B~%F'\"x%bU&r%dZ'p%P&d%`%d";
private static final int KEY = 22;
``` 

After that, we found a function where if the PIN given is correct, it will print out the xorResult which *basically our flag*. Since we know that the params are `HARDCODED_STRING` and also `KEY`, we could write a simple script to do the XOR.

```java
public void onClick(View v) {
	String enteredPin = MainActivity.this.pinInput.getText().toString();
	if (enteredPin.equals(MainActivity.HARDCODED_PIN)) {
	    String xorResult = MainActivity.this.xorString(MainActivity.HARDCODED_STRING, 22);
	    MainActivity.this.resultText.setText(xorResult);
	} else {
	    Toast.makeText(MainActivity.this, "Incorrect PIN!", 0).show();
	}
}

public String xorString(String input, int xorValue) {
	StringBuilder result = new StringBuilder();
	for (char c : input.toCharArray()) {
	    result.append((char) (c ^ xorValue));
	}
	return result.toString();
}
```

## ⚙ Script

```py
enc_flag = "^\"u}B~%F'\"x%bU&r%dZ'p%P&d%`%d"

flag = ''.join(chr(ord(enc_flag[i]) ^ 22) for i in range(len(enc_flag)))
flag = 'CURTIN_CTF{' + flag + '}'

print(flag)
```

## 🏳️ Flag

`CURTIN_CTF{H4ckTh3P14n3tC0d3rL1f3F0r3v3r}`