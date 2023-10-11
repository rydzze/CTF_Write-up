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