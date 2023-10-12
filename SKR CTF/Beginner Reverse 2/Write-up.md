## Beginner Reverse 2

### 📚 Overview

Find the password to get the flag!

```C
#include <stdio.h>

int main () {
	char password[16];
	printf("Enter password: ");
	scanf("%s",password);
	int pass = atoi(password);
	if ((pass*2)-666 == 2008)
	{
		printf("Welcome admin!\nFlag: SKR{%s}",password);
	}else{
		printf("Login failed!");
	}
}
```

### ✨ Solution

The source code will convert the `pass` into integer. Simple math should do the work.

`(pass*2)-666 == 2008`

`pass*2 == 2674`

`pass == 1337`

### 🏳️ Flag

Hence, the flag is `SKR{1337}` 
