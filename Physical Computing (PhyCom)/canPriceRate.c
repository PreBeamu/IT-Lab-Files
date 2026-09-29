#include <stdio.h>

int main() {
    double price, diameter, height;

    scanf("%lf", &price);
    scanf("%lf", &diameter);
    scanf("%lf", &height);
    
    double volume;
    volume = height*3.14159265359*((diameter/2)*(diameter/2));
    
    printf("Volume : %.02fml\n", volume);
    printf("Baht/ml : %.04f\n", price/volume);
    
    return 0;
}