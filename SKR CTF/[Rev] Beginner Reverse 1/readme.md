## Beginner Reverse 1

### 📚 Overview

Warm Up for Reverse Engineering Category: Find the password to get the flag!

```C
#include <stdio.h>

int main () {
	char password[16];
	printf("Enter password: ");
	scanf("%15s",password);
	if (strcmp(password, "P@ssw0rd1337") == 0)
	{
		printf("Welcome admin!\nFlag: SKR{%s}",password);
	}else{
		printf("Login failed!");
	}
}
```

### ✨ Solution

Straightforward question ... If the userInput == "P@ssw0rd1337", it will print the flag.

### 🏳️ Flag

Hence, the flag is `SKR{P@ssw0rd1337}` 
