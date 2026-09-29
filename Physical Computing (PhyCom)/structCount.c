#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char line[500];
    int char_count = 0;
    int word_count = 0;
    int line_count = 0;

    while (1) {
        scanf("%499[^\n]%*c", line);

        int len = strlen(line);
        if (strcmp(line, ".") == 0) {
            break;
        }

        line_count++;

        int in_word = 0;
        for (int i = 0; i < len; i++) {
            if (isalpha(line[i])) {
                char_count++;
            }

            if (!isspace(line[i])) {
                if (!in_word) {
                    in_word = 1;
                    word_count++;
                }
            } else {
                in_word = 0;
            }
        }
    }

    printf("Char = %d, word = %d, line = %d\n", char_count, word_count, line_count);
    return 0;
}