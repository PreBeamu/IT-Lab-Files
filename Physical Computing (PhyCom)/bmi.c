#include <stdio.h>

int main() {
    float height_cm, weight_kg, height_m, bmi;
    scanf("%f", &height_cm);
    scanf("%f", &weight_kg);
    height_m = height_cm / 100.0;
    
    bmi = weight_kg / (height_m * height_m);
    printf("%f\n", bmi);
    
    return 0;
}