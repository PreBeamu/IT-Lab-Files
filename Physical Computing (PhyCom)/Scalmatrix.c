#include <stdio.h>

int main()
{
    double m1[9];
    scanf("%lf %lf %lf", &m1[0], &m1[1], &m1[2]);
    scanf("%lf %lf %lf", &m1[3], &m1[4], &m1[5]);
    scanf("%lf %lf %lf", &m1[6], &m1[7], &m1[8]);

    if (m1[0] == m1[4] && m1[4] == m1[8]) {
        for(int i = 0; i < 9; i++) {
            if (i == 0 || i == 4 || i == 8) {
                continue;
            }
            if (m1[i] != 0) {
                printf("This is not a scalar matrix\n");
                return 0;
            }
        }
        printf("This is a scalar matrix\n");
        return 0;
    } else {
        printf("This is not a scalar matrix\n");
    }

    return 0;
}