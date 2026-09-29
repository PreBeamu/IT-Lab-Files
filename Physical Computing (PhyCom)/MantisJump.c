#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    if (n == 1) {
        printf("method = 1\n");
        return 0;
    }
    
    if (n == 2) {
        printf("method = 2\n");
        return 0;
    }

    long prev_step = 1;
    long curr_step = 2;
    long total_ways = 0;

    for (int i = 3; i <= n; i++) {
        total_ways = prev_step + curr_step;
        prev_step = curr_step;
        curr_step = total_ways;
    }
    printf("method = %lld\n", total_ways);

    return 0;
}