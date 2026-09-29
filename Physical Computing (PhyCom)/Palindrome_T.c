#include <stdio.h>

int main()
{
    char str[101];
    scanf("%100[^\n]", str);

    int size;
    for (int i = 0; i <= 100; i++) {
        if (str[i] == '\0') {
            size = i-1;
            break;
        }
    }

    char rev[size];
    for (int i = 0; i <= size; i++) {
        rev[i] = str[size-i];
    }

    for (int i = 0; i <= size; i++) {
        if (rev[i] != str[i]) {
            printf("It is not Palindrome.");
            return 0;
        }
    }
    printf("It is Palindrome.");
}