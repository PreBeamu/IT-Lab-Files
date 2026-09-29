#include <stdio.h>

int main() {
    char str[205];
    int count[128] = {};
    scanf("%200[^\n]", str);

    for (int i = 0; str[i] != '\0'; i++) {
        if (str[i] != ' ') {
            count[str[i]]++;
        }
    }
    for (int i = 0; i < 128; i++) {
        while (count[i] > 0) {
            printf("%c", i);
            count[i]--;
        }
    }

    return 0;
}