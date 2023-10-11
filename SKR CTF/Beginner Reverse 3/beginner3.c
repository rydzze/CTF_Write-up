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