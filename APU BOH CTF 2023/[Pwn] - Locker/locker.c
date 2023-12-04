#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define LOCKER_NUM 8

size_t n = 32;

typedef struct {
    char key;
    char value;
} locker;

void win() {
    system("cat ./flag.txt");
}

void setup() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

void read_locker(locker *lockers) {
    puts("\n\nRead locker");
    puts("===========");
    puts("Under maintenance");
}

void write_locker(locker *lockers) {
    puts("\n\nWrite Locker");
    puts("===========");
    int number;
    printf("Locker number [1-8]: ");
    scanf("%d", &number);
    if (number > LOCKER_NUM) {
        puts("Under maintenance");
        return;
    }
    printf("Key  : ");
    scanf("%hhd", &lockers[number - 1].key);
    printf("Value: ");
    scanf("%hhd", &lockers[number - 1].value);
}

void menu() {
    puts("\n\nLocker");
    puts("======");
    puts("1. Read");
    puts("2. Write");
    puts("3. Exit");
}

int main(void) {
    setup();
    locker lockers[LOCKER_NUM];
    memset(lockers, 0, sizeof(lockers));
    int option;
    do {
        option = 0;
        menu();
        printf("> ");
        scanf("%d", &option);
        switch (option) {
        case 1:
            read_locker(lockers);
            break;
        case 2:
            write_locker(lockers);
            break;
        default:
            break;
        }
    } while (option == 1 || option == 2);
    while (getchar() != '\n')
        ;
    char feedback[32];
    puts("Feedback?");
    scanf("%s", feedback);
    return 0;
}
