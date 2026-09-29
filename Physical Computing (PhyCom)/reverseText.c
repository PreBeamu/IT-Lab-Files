#include <stdio.h>

int main()
{
    char str[101] = ""; 
    scanf("%100[^\n]", str); 
    
    int str_size = 0;
    for(int i = 0; i <= 100; i++) {
        if (str[i] == '\0') {
            str_size = i;
            break;
        }
    }
    
    for(int i = str_size - 1; i >= 0; i--) {
        printf("%c", str[i]);
    }
    
    return 0;
}