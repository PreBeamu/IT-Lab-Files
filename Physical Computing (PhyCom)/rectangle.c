#include <stdio.h>

int main() {
    double width, length;
    double area, perimeter;
    
    scanf("%lf", &width);
    scanf("%lf", &length);
    
    perimeter = 2 * (width + length);
    printf("Perimeter of rectangle = %.4f units\n", perimeter);
    
    return 0;
}