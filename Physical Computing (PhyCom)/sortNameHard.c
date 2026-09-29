#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

int compare_names(const void *a, const void *b) {
    const char *str1 = (const char *)a;
    const char *str2 = (const char *)b;
    
    int k;
    for (k = 0; str1[k] != '\0' || str2[k] != '\0'; k++) {
        if (str1[k] != str2[k]) {
            return str1[k] - str2[k];
        }
    }
    
    return 0;
}

int main() {
    int stu_size;
    scanf("%d", &stu_size);
    char names[stu_size][65];
    int i, j;

    for (i = 0; i < stu_size; i++) {
        scanf(" %[^\n]", names[i]);
        
        int newWord = 1;
        for (j = 0; names[i][j] != '\0'; j++) {
            if (isspace(names[i][j])) {
                newWord = 1;
            } else if (newWord) {
                names[i][j] = toupper(names[i][j]); 
                newWord = 0;
            } else {
                names[i][j] = tolower(names[i][j]);
            }
        }
    }
    qsort(names, stu_size, 65, compare_names);

    for (i = 0; i < stu_size; i++) {
        printf("%s\n", names[i]);
    }

    return 0;
}