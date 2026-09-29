#include <stdio.h>

int main() {
    char model_name[100];
    scanf(" %[^\n]", model_name);

    int n;
    scanf("%d", &n);

    int speeds[15];
    for (int i = 0; i < n; ++i) {
        scanf("%d", &speeds[i]);
    }

    int current_speed;
    scanf("%d", &current_speed);

    printf("%s\n", model_name);

    if (current_speed > speeds[n - 1]) {
        printf("> %d\n", speeds[n - 1]);
    } 
    else if (current_speed <= speeds[0]) {
        printf("%d - %d\n", speeds[0], speeds[1]);
    } 
    else {
        for (int i = 1; i < n; ++i) {
            if (current_speed > speeds[i - 1] && current_speed <= speeds[i]) {
                printf("%d - %d\n", speeds[i - 1], speeds[i]);
                break;
            }
        }
    }

    return 0;
}