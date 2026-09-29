#include <stdio.h>
 
int main()
{
    double m1[9];
    scanf("%lf %lf %lf", &m1[0], &m1[1], &m1[2]);
    scanf("%lf %lf %lf", &m1[3], &m1[4], &m1[5]);
    scanf("%lf %lf %lf", &m1[6], &m1[7], &m1[8]);
    
    double m2[9];
    scanf("%lf %lf %lf", &m2[0], &m2[1], &m2[2]);
    scanf("%lf %lf %lf", &m2[3], &m2[4], &m2[5]);
    scanf("%lf %lf %lf", &m2[6], &m2[7], &m2[8]);
    
    printf("A x B\n");
    double result[9];
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            result[i * 3 + j] = 0;
            for (int k = 0; k < 3; k++) {
                result[i * 3 + j] += m1[i * 3 + k] * m2[k * 3 + j];
            }
            printf("%.2lf ", result[i * 3 + j]); 
        }
        printf("\n");
    }
    
    
    return 0;
}