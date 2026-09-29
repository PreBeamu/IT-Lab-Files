#include <stdio.h>
#include <math.h>
 
int main() {
    int theta, u;
    double radian, h;
    double PI = 3.141592653589793;
    double g = 9.81;
 
    scanf("%d", &theta);
    scanf("%d", &u);
 
    radian = (theta * PI) / 180.0;
    h = (u * u * sin(radian) * sin(radian)) / (2.0 * g);
 
    printf("theta (degree) : %d\n", theta);
    printf("u (m/s) : %d\n", u);
    printf("h (m) : %.4lf\n", h);
 
    return 0;
}