#include <stdio.h>
#include <math.h>

int main() {
    double a, b, c;
    
    scanf("%lf", &a);
    scanf("%lf", &b);
    
    c = sqrt(a * a + b * b);
    
    printf("%.2f\n", c);
    
    return 0;
}