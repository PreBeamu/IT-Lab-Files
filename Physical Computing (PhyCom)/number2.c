#include <stdio.h>

int main(){
        char input[6];
        scanf(" %5c",input);
    
        printf("%c", input[0]);
        printf("%81c%c", input[0], input[1]);
        printf("%80c%c%c", input[0], input[1], input[2]);
        printf("%79c%c%c%c", input[0], input[1], input[2], input[3]);
        printf("%78c%c%c%c%c", input[0], input[1], input[2], input[3], input[4]);
        return 0;
}

