#include <stdio.h>

int main() {
    double mph, kmh;
    scanf("%lf", &mph);
    
    kmh = mph * 1.60934;
    printf("%.2f\n", kmh);
    
    return 0;
}