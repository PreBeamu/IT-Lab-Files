#include <stdio.h>
#include <string.h>

int main() {
    char str[101];
    char temp[101];

    scanf("%100[^\n]", str);

    while (1) {
        int len = strlen(str);
        int found = 0;
        int i = 0;
        int k = 0;

        while (i < len) {
            if (i + 1 < len && str[i] == str[i + 1]) {
                found = 1;
                i += 2;
            } else {
                temp[k++] = str[i];
                i++;
            }
        }

        temp[k] = '\0';

        if (!found) {
            break;
        }

        strcpy(str, temp);
        printf("%s\n", str);
    }

    return 0;
}