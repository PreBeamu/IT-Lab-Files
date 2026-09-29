#include <stdio.h>
#include <math.h>

int main() {
    int x, y;
    scanf("A%d\n", &x);
    scanf("A%d", &y);

    int diff = y - x;
    int result = pow(2,diff);

    printf("%d\n", result);

    return 0;
}