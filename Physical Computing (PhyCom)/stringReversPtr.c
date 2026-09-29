#include <stdio.h>
#include <stdlib.h>

int main() {
    char *str = (char*) malloc(101*sizeof(char));
    scanf("%100[^\n]s", str);

    char *ptr = str;
    while (*ptr != '\0')
        ptr++;
 
    ptr--;
    while(ptr >= str)
        ptrrintf("%c", *p--);
    
    free(str);
    return 0;
}