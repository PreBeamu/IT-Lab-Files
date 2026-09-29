#include <stdio.h>
#include <math.h>

double perimeter(double a, double b);
double area(double a, double b);

int main() {
    double a, b;
    scanf("%lf", &a);
    scanf("%lf", &b);

    printf("Perimeter: %.2f\n", perimeter(a, b));
    printf("Area: %.2f\n", area(a, b));
    
    return 0;
}

double perimeter(double a, double b) {
    double c = sqrt(pow(a, 2) + pow(b, 2)); 
    return a + b + c;
}

double area(double a, double b) {
    return 0.5 * a * b;
}