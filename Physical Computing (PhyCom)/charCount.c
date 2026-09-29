#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

int main() {
    char *str = (char*) malloc(101*sizeof(char));
    scanf("%100[^\n]s", str);

    int low = 0,up = 0,dig = 0;
    int i = 0;
    while (*(str + i) != '\0') {
        if (isdigit(*(str + i))) {
            dig++;
        } else if (islower(*(str + i))) {
            low++;
        } else if (isupper(*(str + i))) {
            up++;
        }
        i++;
    }

    printf("Lowercase letters: %d\nUppercase letters: %d\nDigits: %d\n", low, up, dig);
    
    free(str);
    return 0;
}