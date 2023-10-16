## Beginner Reverse 5

### 📚 Overview

Find the correct password to get the flag!

```C
int checkPassword(char* pass){
	size_t length = strlen(pass);
	if(length != 14){
		return 0;
	}
	char* correct_pass = "BTDJJ`Qmvt`1o4";
	for (int i = 0; i < length; i++){
		if(pass[i] != correct_pass[i]-1){
			return 0;
		}
	}
	return 1;
}
```

### 🤔 Hint 

> _"What is [ASCII](http://www.asciitable.com/)?"_

### ✨ Solution

Subtract the decimal value for each ASCII character inside `correct_pass`. You may write a short script to calculate it automatically.

```C
  pass[0] == 'A'
  pass[1] == 'S'
  pass[2] == 'C'
  pass[3] == 'I'
  pass[4] == 'I'
  pass[5] == '_'
  pass[6] == 'P'
  pass[7] == 'l'
  pass[8] == 'u'
  pass[9] == 's'
  pass[10] == '_'
  pass[11] == '0'
  pass[12] == 'n'
  pass[13] == '3'
```

### 🏳️ Flag

Hence, the flag is `SKR{ASCII_Plus_0n3}` 
