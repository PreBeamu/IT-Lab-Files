#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Record {
    char id[10];
    char name[100];
    long salary;
    long sales;
};

int main() {
    int n;
    scanf("%d", &n);
    
    struct Record rec[n];
    for (int i = 0; i < n; i++) {
        scanf("%s %s %ld %ld", rec[i].id, rec[i].name, &rec[i].salary, &rec[i].sales);
    }
    
    char search_id[10];
    scanf("%s", search_id);
    
    int found = 0;
    for (int i = 0; i < n; i++) {
        if (strcmp(rec[i].id, search_id) == 0) {
            printf("%s\n", rec[i].id);
            printf("%s\n", rec[i].name);
            printf("%ld\n", rec[i].sales);
            printf("%.02lf\n", rec[i].sales*0.02);
            printf("%ld\n", rec[i].salary);
            printf("%.02lf\n", (rec[i].sales*0.02)+rec[i].salary);
            found = 1;
            break;
        }
    }

    if (!found) {
        printf("ID not found !!!\n");
    }

    return 0;
}