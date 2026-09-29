#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

int cmp(const void *vp, const void *vq);

int main()
{
    int stu_size;
    scanf("%d", &stu_size);

    char names[stu_size][61];
    for (int i=0; i<stu_size; i++) {
        scanf(" %60[^\n]", names[i]);

        int name_size;
        for (int j=0; j<=60; j++) {
            if (names[i][j] == '\0') {
                name_size = j;
                break;
            }
        }

        int new_word = 1;
        for (int j=0; j<name_size; j++) {
            if (names[i][j] == ' ') {
                new_word = 1;
            } else {
                if (new_word == 1) {
                    new_word = 0;
                    names[i][j] = toupper(names[i][j]);
                } else {
                    names[i][j] = tolower(names[i][j]);
                }
            }
        }
    }

    qsort(names, stu_size, sizeof(names[0]), cmp);

    for (int i=0; i<stu_size; i++) {
        printf("%s\n", names[i]);
    }
}

int cmp(const void *vp, const void *vq)
{
    const char *p = vp;
    const char *q = vq;

    int i = 0;
    while (p[i] != '\0' && q[i] != '\0') {
        if (p[i] != q[i]) {
            return (p[i] - q[i]);
        }
        i++;
    }
    return (p[i] - q[i]);
}