#include <stdio.h>
#include <stdlib.h>

char name[0x10];

void safe(void) {
    system("echo -n 'What is your name? '");
    gets(name);
}

void vuln(void) {
    char buf[0x10];
    system("echo -n 'Are you running M1? '");
    gets(buf);
}

void setup() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

int main(void) {
    setup();
    system("echo -n 'Choose wisely\n1. safe\n2. vuln\n> ' ");
    unsigned int choice;
    scanf("%d%*c", &choice);
    switch (choice) {
    case 1:
        safe();
        break;
    case 2:
        vuln();
        break;
    default:
        break;
    }
    return 0;
}
