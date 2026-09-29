#include <stdio.h>
#include <string.h>

void print_centered(int width, char *text) {
    int len = strlen(text);
    int inner_space = width - 2;
    int total_spaces = inner_space - len;
    int left_spaces = (total_spaces + 1) / 2;
    int right_spaces = total_spaces - left_spaces;

    printf("*");
    for (int i = 0; i < left_spaces; i++) {
        printf(" ");
    }
    printf("%s", text);
    for (int i = 0; i < right_spaces; i++) {
        printf(" ");
    }
    printf("*\n");
}

int main() {
    int width;
    char text1[60];
    char text2[50];

    scanf("%d\n", &width);
    scanf("%[^\n]\n", text1);
    scanf("%[^\n]", text2);

    for (int i = 0; i < width; i++) {
        printf("*");
    }
    printf("\n");

    print_centered(width, text1);
    print_centered(width, text2);

    for (int i = 0; i < width; i++) {
        printf("*");
    }
    printf("\n");

    return 0;
}