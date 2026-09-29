#include <stdio.h>
#include <ctype.h>

int main() {
    char name[201];
    scanf("%200[^\n]", name);

    char fn = name[0], ln;
    for (int i = 0; name[i] != '\0'; i++) {
        if (isspace(name[i])) {
            ln = name[i+1];
            break;
        }
    }

    printf("%c.%c.\n", fn, ln);

    return 0;
}