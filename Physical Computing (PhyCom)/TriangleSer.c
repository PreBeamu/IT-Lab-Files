#include <stdio.h>

int main() {
    unsigned int n;
    unsigned int sum = 0;
    
    scanf("%u", &n);
    for (unsigned int i = 1; i <= n; i++) {
        sum += i;
    }
    printf("%u\n", sum);
    
    return 0;
}