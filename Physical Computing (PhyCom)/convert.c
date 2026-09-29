#include <stdio.h>
#include <ctype.h>

int main() {
    char str[2][101];
    scanf(" %100[^\n]", str[0]);
    scanf(" %100[^\n]", str[1]);

    printf("*** Results ***\n");

    for(int i = 0; str[0][i] != '\0'; i++) {
        if (str[0][i] >= 'a' && str[0][i] <= 'z') {
            str[0][i] = toupper(str[0][i]);
        } else if (str[0][i] >= 'A' && str[0][i] <= 'Z') {
            str[0][i] = tolower(str[0][i]);
        }
        printf("%c", str[0][i]);
    }
    
    printf("\n");
    
    for(int i = 0; str[1][i] != '\0'; i++) {
        if (str[1][i] >= 'a' && str[1][i] <= 'z') {
            str[1][i] = toupper(str[1][i]);
        } else if (str[1][i] >= 'A' && str[1][i] <= 'Z') {
            str[1][i] = tolower(str[1][i]);
        }
        printf("%c", str[1][i]);
    }

    printf("\n");
    printf("***************\n");

    for(int i = 0; str[0][i] != '\0' || str[1][i] != '\0'; i++) {
        if (tolower(str[0][i]) != tolower(str[1][i])) {
            printf("Both strings are not the same.");
            return 0;
        }
    }
    
    printf("Both strings are the same.");

    return 0;
}