#include <stdio.h>

int main() {
    double f1;
    scanf("%lf", &f1);
    double f2;
    scanf("%lf", &f2);
    double f3;
    scanf("%lf", &f3);
    double f4;
    scanf("%lf", &f4);
    
    printf("Summation is %.2lf\n", f1+f2+f3+f4);
    printf("Average is %.3lf", (f1+f2+f3+f4)/4);
    return 0;
}