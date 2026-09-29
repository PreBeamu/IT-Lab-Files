#include <stdio.h>

int main() {
    char tire;

    scanf("%c", &tire);

    switch (tire) {
        case 's': 
        case 'S':
            printf("Soft");
            break;
        case 'm': 
        case 'M':
            printf("Medium");
            break;
        case 'h': 
        case 'H':
            printf("Hard");
            break;
        case 'i': 
        case 'I':
            printf("Intermediate");
            break;
        case 'w': 
        case 'W':
            printf("Wet");
            break;
    }

    return 0;
}