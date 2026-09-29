#include <stdio.h>
#include <ctype.h>

int main() {
    char target;
    char text[151];

    scanf("%c\n", &target);
    scanf("%150[^\n]", text);
    char targetL = tolower(target);

    int count = 0;
    for (int i = 0; text[i] != '\0'; i++) {
        if (tolower(text[i]) == targetL) {
            count++;
        }
    }

    printf("%d\n", count);

    return 0;
}