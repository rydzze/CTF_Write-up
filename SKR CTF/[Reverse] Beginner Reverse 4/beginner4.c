#include <stdio.h>
#include <string.h>

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