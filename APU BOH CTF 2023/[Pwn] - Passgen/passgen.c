#include <fcntl.h>
#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define PASSWORD_SIZE 0x40
#define SALT_WEIGHT 0x20
#define DEBUG_KEY_SIZE 0x40

int urandom_fd, passwd_fd;
int debug_mode = 0;
char debug_key[DEBUG_KEY_SIZE];
char password[PASSWORD_SIZE + 1];

void debug_print(const char *msg, size_t msg_len, ...) {
    if (!debug_mode) {
        return;
    }
    va_list args;
    va_start(args, msg_len);
    char *debug_msg = calloc(1, msg_len + 0x10);
    strcat(debug_msg, "[DEBUG] ");
    strcat(debug_msg, msg);
    vprintf(debug_msg, args);
    va_end(args);
    free(debug_msg);
}

void win() {
    system("cat flag.txt");
}

void getint(unsigned int *out) {
    scanf("%u", out);
    while (getchar() != '\n')
        ;
}

void rotate_key() {
    char key[DEBUG_KEY_SIZE];
    read(urandom_fd, key, DEBUG_KEY_SIZE);
    for (size_t i = 0; i < DEBUG_KEY_SIZE; i += 2) {
        snprintf(&key[i], 2, "%x", (unsigned char)key[i]);
    }
    memcpy(debug_key, key, DEBUG_KEY_SIZE);
}

void enable_debug_mode() {
    printf("debug key: ");
    char key[DEBUG_KEY_SIZE + 1];
    char fmt[8];
    sprintf(fmt, "%%%ds", DEBUG_KEY_SIZE);
    scanf(fmt, key);
    if (!memcmp(debug_key, key, DEBUG_KEY_SIZE)) {
        puts("debug mode enabled");
        debug_mode = 1;
    }
}

void gen_pass(char *salt, size_t salt_len) {
    memset(password, 0, PASSWORD_SIZE);
    char pepper[PASSWORD_SIZE];
    read(urandom_fd, pepper, PASSWORD_SIZE);
    for (size_t i = 0; i < PASSWORD_SIZE; i += 2) {
        char temp[3];
        snprintf(temp, 3, "%02x", (unsigned char)pepper[i]);
        memcpy(&pepper[i], temp, 2);
    }
    memcpy(password, pepper, PASSWORD_SIZE);
    do {
        printf("salt: ");
        int nbytes = read(0, salt, salt_len);
        if (nbytes == salt_len) {
            break;
        }
        puts("Not enough salt, your password is underseasoned");
    } while (1);
    memcpy(password, salt, salt_len);
}

void save_pass() {
    write(passwd_fd, password, PASSWORD_SIZE);
    puts("password saved to /tmp/passgen.txt");
}

void menu() {
    puts("Passgen v0.1");
    puts("1. Generate password");
    puts("2. View password");
    puts("3. Save password");
    puts("4. Debug mode");
    puts("0. Exit");
    int valid = 1;
    do {
        char salt[SALT_WEIGHT];
        unsigned int choice;
        printf("> ");
        getint(&choice);
        switch (choice) {
        case 1:
            gen_pass(salt, SALT_WEIGHT);
            break;
        case 2:
            puts("TODO: View password");
            debug_print(password, PASSWORD_SIZE);
            break;
        case 3:
            save_pass();
            break;
        case 4:
            rotate_key();
            enable_debug_mode();
            break;
        default:
            valid = 0;
            break;
        }
    } while (valid);
    close(urandom_fd);
    close(passwd_fd);
    char bug_report[0256];
    printf("Did you find any bug? ");
    fgets(bug_report, 256, stdin);
    exit(EXIT_SUCCESS);
}

void setup() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

int main(void) {
    setup();
    urandom_fd = open("/dev/urandom", O_RDONLY);
    passwd_fd = open("/tmp/passgen.txt", O_WRONLY);
    menu();
    return 0;
}
