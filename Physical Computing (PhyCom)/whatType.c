#include <stdio.h>

int main()
{
    char input;
    scanf("%c", &input);
    int asc_code = input;
    
    if (asc_code >= 97 && asc_code <= 122){
        printf("lowercase");
    } else if (asc_code >= 65 && asc_code <= 90){
        printf("uppercase");
    } else if (asc_code >= 48 && asc_code <= 57){
        printf("number");
    } else {
        printf("error");
    }
    
    return 0;
}