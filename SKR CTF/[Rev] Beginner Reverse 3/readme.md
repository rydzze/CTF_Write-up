## Beginner Reverse 3

### 📚 Overview

Find the password to get the flag!

```C
#include <stdio.h>
#include <string.h>

int checkPassword(char* pass){
	if(strlen(pass) != 14){
		return 0;
	}
	if(strncmp(pass+2,"cur3", 4) != 0){
		return 0;
	}
	if(strncmp(pass,"S3", 2) != 0){
		return 0;
	}
	if(strncmp(pass+10,"w0rd", 4) != 0){
		return 0;
	}
	if(strncmp(pass+6,"Pa$$", 4) != 0){
		return 0;
	}
	return 1;
}


int main () {
	char password[20];
	printf("Enter password: ");
	scanf("%19s",password);
	if (checkPassword(password))
	{
		printf("Welcome admin!\nFlag: SKR{%s}",password);
	}else{
		printf("Login failed!");
	}
}
```

### ✨ Solution

The password length should be 14, and there are 4 parts in total where
- part1 = S3
- part2 = cur3
- part3 = Pa$$
- part4 = w0rd

So, combine all the parts together and you will get the password.

### 🏳️ Flag

Hence, the flag is `SKR{S3cur3Pa$$w0rd}` 
