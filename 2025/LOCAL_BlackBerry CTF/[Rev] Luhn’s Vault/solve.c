#include <stdio.h>
#include <string.h>

unsigned char *decryptFlag(const unsigned char *input, int len, unsigned char *flag) {
    for (int i = 0; i < len; ++i) {
        unsigned char temp = input[i] ^ 0xAA;
        flag[i] = (temp >> 2) | (temp << 6);
    }
    flag[len] = '\0';
    return flag + len;
}

int main() {
    unsigned char enc_flag[] = {0x9B, 0xFF, 0x26, 0x93, 0xD7, 0xB7, 0x97, 0xFB, 0xD7, 0xBF, 0xEB, 0xA3, 0xAF, 0x97, 0xA7, 0x9F, 0xEF};
    int len_flag = sizeof(enc_flag);

    unsigned char flag[len_flag + 1];
    decryptFlag(enc_flag, len_flag, flag);

    printf("Flag: bbctf{%s}", flag);

    return 0;
}