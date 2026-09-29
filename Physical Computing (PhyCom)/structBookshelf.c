#include <stdio.h>
#include <string.h>

struct Book {
    char id[10];
    char name[100];
    char author[100];
};

int main() {
    int n;
    scanf("%d", &n);

    char search_id[10];
    scanf("%s", search_id);

    struct Book books[n];
    for (int i = 0; i < n; i++) {
        scanf("%s %s %s", books[i].id, books[i].name, books[i].author);
    }

    int found = 0;
    for (int i = 0; i < n; i++) {
        if (strcmp(books[i].id, search_id) == 0) {
            printf("%s %s %s\n", books[i].id, books[i].name, books[i].author);
            found = 1;
            break;
        }
    }

    if (!found) {
        printf("Not Found\n");
    }

    return 0;
}