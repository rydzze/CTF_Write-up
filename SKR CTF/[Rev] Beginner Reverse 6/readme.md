## Beginner Reverse 6

### 📚 Overview

Find the correct password to get the flag!

```C
int checkPassword(char* pass){
	size_t length = strlen(pass);
	if(length != 17){
		return 0;
	}
	if(pass[0] != 'R'){
		return 0;
	}
	if(pass[1] - pass[0] != -31 || pass[1] != pass[3]){
		return 0;
	}
	if(pass[4] != tolower(pass[0]) || pass[2] - pass[4] != 4){
		return 0;
	}
	if(pass[5] != '5' || pass[5] - pass[6] != 4){
		return 0;
	}
	if(pass[7] != pass[0] + 28 || pass[2] - pass[8] != 47){
		return 0;
	}
	if(pass[9] != '_' || pass[12] != pass[9] || strncmp(pass+13,"Fun!",4) != 0 || strncmp(pass+10,"1s",2) != 0){
		return 0;
	}
	return 1;
}
```

### ✨ Solution

Involve math operation of decimal value of ASCII character, refer [Beginner Reverse 5](https://github.com/rydzze/CTF_Write-up/tree/61308d9e6068ec8fa1d84c724c03565cc4569f53/SKR%20CTF/Beginner%20Reverse%205).

```C
  pass[0] == 'R'
  pass[1] == '3'
  pass[2] == 'v'
  pass[3] == '3'
  pass[4] == 'r'
  pass[5] == '5'
  pass[6] == '1'
  pass[7] == 'n'
  pass[8] == 'G'
  pass[9] == '_'
  pass+10 == "1s"
  pass[12] == '_'
  pass+13 == "Fun!"
```

### 🏳️ Flag

Hence, the flag is `SKR{R3v3r51nG_1s_Fun!}` 
