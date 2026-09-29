#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    int freq[256] = {0};
    char order[256];
    int unique_count = 0;

    for (int i = 0; i < n; i++) {
        char c;
        scanf(" %c", &c);
        
        c = c + 32 * (c >= 'A' && c <= 'Z');
        
        order[unique_count] = c;
        unique_count += (freq[c] == 0);
        freq[c]++;
    }

    for (int i = 0; i < unique_count; i++) {
        printf("%c: %d\n", order[i], freq[order[i]]);
    }

    return 0;
}