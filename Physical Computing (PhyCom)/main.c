#include <stdio.h>

int main()
{
    char str[101];
    scanf("%[^\n]", &str);
    
    int str_size = 0;
    for(int i=0; i<100; i++) {
        if (str[i]=='\0') {
            str_size = i;
            break;
        }
    }
    
    for(int i=0; i<=str_size; i++) {
        if (str[str_size-i]!='\0') {
            printf("%c", str[str_size-i]);
        }
    }
    
    return 0;
}