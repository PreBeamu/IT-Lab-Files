#include <stdio.h>

int main() {
    char str[151];
    scanf("%150[^\n]", str);

    for (int i = 0; str[i] != '\0'; i++) {
        if (str[i] != ' ') {
            printf("%c", str[i]);
        }
    }

    return 0;
}