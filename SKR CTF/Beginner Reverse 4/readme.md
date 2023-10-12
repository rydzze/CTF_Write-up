## Beginner Reverse 1

### 📚 Overview

Find the correct password to get the flag!

```C
int checkPassword(char* pass){
	size_t length = strlen(pass);
	if(length != 15){
		return 0;
	}
	char* part1 = "Spr3ue45";
	for (int i = 0, j = 0; i < length; i+=2,j++){
		if(pass[i] != part1[j]){
			return 0;
		}
	}

	char* part2 = "5PrcS3u";
	for (int i = length-2, j = 0; i > 0; i-=2,j++){
		if(pass[i] != part2[j]){
			return 0;
		}
	}
	return 1;
}
```

### 🤔 Hint 

> _"Keep track of the increment and decrement of i and j"_

### ✨ Solution

```C
//First for loop
  pass[0] == part1[0] 
  pass[2] == part1[1]
  pass[4] == part1[2]
  pass[6] == part1[3]
  pass[8] == part1[4]
  pass[10] == part1[5]
  pass[12] == part1[6]
  pass[14] == part1[7]

//Second for loop 
  pass[13] == part2[0] 
  pass[11] == part2[1]
  pass[9] == part2[2]
  pass[7] == part2[3]
  pass[5] == part2[4]
  pass[3] == part2[5]
  pass[1] == part2[6]

//Sup3rS3cureP455
```

### 🏳️ Flag

Hence, the flag is `SKR{Sup3rS3cureP455}` 
