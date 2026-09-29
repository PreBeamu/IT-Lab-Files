#include <stdio.h>

int main() {
    char chars[5];
    
    for (int i=0; i<5; i++){
    	scanf(" %c", &chars[i]);
    }

    chars[0] = chars[0] + 1;
    chars[2] = chars[2] + 1;
    chars[4] = chars[4] + 1;

    for (int i=0; i<5; i++){
        printf("%c\n", chars[i]);
    }
    
    return 0;
}
