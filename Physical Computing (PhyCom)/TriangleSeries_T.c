#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);

    unsigned int sum = 0;
    for (int i=1; i<=n; i++) {
        sum += i;
    }

    printf("%u", sum);
}