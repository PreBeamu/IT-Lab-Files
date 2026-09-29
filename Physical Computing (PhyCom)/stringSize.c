#include <stdio.h>
#include <stdlib.h>

int main() {
    char *str = (char*) malloc(101*sizeof(char));
    scanf("%100[^\n]s", str);

    int size = 0;
    while (*(str + size) != '\0') {
        size++;
    }

    printf("%d\n", size);
    
    free(str);
    return 0;
}