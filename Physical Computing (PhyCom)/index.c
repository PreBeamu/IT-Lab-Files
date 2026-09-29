#include <stdio.h>
int M[] = {2, 20, 8, 10, 4, 6, 16, 18};
int N[] = {1, 3, 9, 7, 11, 15, 19};
 
int main()
{
    int num;
    while (num < 1 || num > 20) {
        scanf("%d", &num);
    }
     
    for (int i=0; i<8; i++){
        if (M[i]==num){
            printf("%d is in M at index [%d]", num, i);
            return 0;
        }
    }
    for (int x=0; x<7; x++){
        if (N[x]==num){
            printf("%d is in N at index [%d]", num, x);
            return 0;
        }
    }
     
    printf("%d is not in neither M nor N", num);
    return 0;
}