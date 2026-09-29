#include <stdio.h>

int main()
{
    char alpha;
    scanf("%c", &alpha);
    
    int asc_code = alpha;
    if (asc_code >= 97 && asc_code <= 122){
        printf("%c", alpha - 32);
    } else if (asc_code >= 65 && asc_code <= 90){
        printf("%c", alpha + 32);
    } else {
        printf("error");
    }
    
    return 0;
}