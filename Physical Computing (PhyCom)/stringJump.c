#include <stdio.h>
#include <stdlib.h>

int main() {
    unsigned int size, modz;
    scanf("%u", &size);
    scanf("%u", &modz);
    
    char *str = (char*) malloc(size*sizeof(char));
    scanf(" %[^\n]s", str);

    int i = 0;
    while (*(str + i) != '\0') {
        if (i%modz == 0) {
            printf("%c", *(str + i));
        }
        i++;
    }
    
    free(str);
    return 0;
}