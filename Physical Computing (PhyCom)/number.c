#include <stdio.h>

int main() {
        char input[6];
        char digits[5];
        scanf("%5c",input);

        digits[0] = input[2];
        digits[1] = input[3];
        digits[2] = input[4];
        digits[3] = input[0];
        digits[4] = input[1];

        for(int i=0; i<5; i++){
                printf("%c",digits[i]);
        };

        return 0;
}
