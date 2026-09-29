#include <stdio.h>

int main()
{
    int safe, lap, sout;
    float distance;

    scanf("%d", &safe);
    scanf("%f", &distance);
    scanf("%d", &lap);
    scanf("%d", &sout);

    int invalid = 0;

    if (safe == 0) {
        invalid += 1;
    }
    if (lap <= 2) {
        invalid += 1;
    }
    if ((lap - sout) <= 1) {
        invalid += 1;
    }
    if (distance >= 1.0) {
        invalid += 1;
    }
    if (invalid > 0) {
        printf("DRS not allowed %d", invalid);
    } else {
        printf("DRS allowed");
    }

    return 0;
}