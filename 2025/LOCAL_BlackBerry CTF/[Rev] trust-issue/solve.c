#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void hex_to_string(const char *input, char *output) {
    size_t input_length = strlen(input);
    unsigned int output_index = 0;

    for (unsigned int i = 0; i < input_length; i += 2) {
        if ((i % 4) == 0 && (i + 1) < input_length && output_index < 0x63) {
            char temp[3];
            temp[0] = input[i];
            temp[1] = input[i + 1];
            temp[2] = '\0';

            output[output_index++] = (char)strtol(temp, NULL, 16);
        }
    }
}

int main() {
    const char *hex_str = "4ea3305c749f5fd241b7314a31885ff633e46e7a74c9723b79915f55530d74a63462722e743973be5f11465a728930ce6d6f5f374d3e3471311c4e";
    char flag[100];
    
    hex_to_string(hex_str, flag);

    printf("Flag: bbctf{%s}", flag);

    return 0;
}