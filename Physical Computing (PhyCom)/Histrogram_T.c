#include <stdio.h>
#include <ctype.h>

int main()
{
    int x, amount;
    scanf("%d", &x);

    int freq[256] = {0};
    char order[256];
    int unique_c = 0;

    for (int i = 0; i < x; i++) {
        char c;
        scanf(" %c", &c);

        c = tolower(c);

        if (freq[c] == 0) {
            order[unique_c] = c;
            unique_c++;
        }

        freq[c]++;
    }

    for (int i = 0; i < unique_c; i++) {
        printf("%c: %d\n",order[i], freq[order[i]]);
    }
}