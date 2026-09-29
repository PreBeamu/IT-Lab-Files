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
    
    char txt[101] = ""; 
    for(int i = str_size - 1; i >= 0; i--) {
        txt[str_size - 1 - i] = str[i];
    }
    
    for(int i = 0; i < str_size; i++) {
        if (str[i] != txt[i]) {
            printf("It is not Palindrome.\n");
            return 0;
        }
    }
    
    printf("It is Palindrome.\n");
    return 0;
}