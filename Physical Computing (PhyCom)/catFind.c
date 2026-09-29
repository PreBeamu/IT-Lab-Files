#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char text[2001];
    char lower_text[2001];

    scanf("%2000[^\n]", text);

    for (int i = 0; text[i] != '\0'; i++) {
        lower_text[i] = tolower(text[i]);
    }

    char *ptr = strstr(lower_text, "cat");
    int first = 1;

    while (ptr != NULL) {
        int index = ptr - lower_text;
        if (!first) {
            printf(", ");
        }
        printf("%d", index);
        first = 0;

        ptr = strstr(ptr + 1, "cat");
    }
    printf("\n");

    return 0;
}