#include <stdio.h>
#include <math.h>

int main() {
    long x, y;
    scanf("%lld %lld", &x, &y);

    double c = sqrt((double)x * x + (double)y * y);
    printf("sqrt(%lld^2+%lld^2)=%.2f\n", x, y, c);
    
    return 0;
}