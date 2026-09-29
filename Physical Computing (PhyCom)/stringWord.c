#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char text[155];
    char words[100][155];
    int word_count = 0;
    scanf("%150[^\n]", text);

    char *token = strtok(text, " ");
    while (token != NULL) {
        for (int i = 0; token[i] != '\0'; i++) {
            token[i] = tolower(token[i]);
        }
        strcpy(words[word_count], token);
        word_count++;
        token = strtok(NULL, " ");
    }

    printf("%d words\n", word_count);
    printf("----\n");

    for (int i = 0; i < word_count; i++) {
        printf("%s : %zu\n", words[i], strlen(words[i]));
    }

    return 0;
}