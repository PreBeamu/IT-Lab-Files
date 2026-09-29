#include <stdio.h>
#include <ctype.h>

char DPT[] = {
    'Q','R','M','N','C','E','D','K','L','J',
    'O','S','H','T','U','F','V','Z','G','W',
    'I','A','B','X','Y','P'
};

int main()
{
    char str[201];
    scanf("%200[^\n]", str);

    int size = 0;
    for(int i = 0; i <= 200; i++) {
        if (str[i] == '\0') {
            size = i;
            break;
        }
    }

    for (int i = 0; i <= size; i++) {
        if (str[i] == ' ') {
            printf("%c", str[i]);
            continue;
        }
        for (int j = 0; j < 26; j++) {
            if (str[i] == DPT[j]) {
                printf("%c",DPT[(j + 5)%26]);
            } else if (str[i] == tolower(DPT[j])) {
                printf("%c",tolower(DPT[(j + 5)%26]));
            }
        }
    }

    return 0;
}