#include <stdio.h>

int main() {
        char first[30];
        char sec[30];
        char third[30];
        char fourth[30];

        scanf("%s",&first);
        scanf("%s",&sec);
        scanf("%s",&third);
        scanf("%s",&fourth);

        printf("String 1: %.3s\n",first);
        printf("String 2: %.4s\n",sec);
        printf("String 3: %.5s\n",third);
        printf("String 4: %.6s\n",fourth);
        return 0;
}
