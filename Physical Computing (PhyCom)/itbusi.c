#include <stdio.h>

int main() {
    float cash, bank;
    scanf("%f", &bank);
    scanf("%f", &cash);
    
    int failed = 0;
    while(1) {
        if (failed >= 3) {
            break;
        }
        
        char action;
        float num;
        scanf("%c %f", &action, &num);
        
        if (action == 'E') {
            break;
        }
        
        if (action == 'D') {
            if (cash < num) {
                failed++;
            } else {
                cash -= num;
                bank += num;
                failed = 0;
            }
        }
        
        if (action == 'W') {
            if (bank < num) {
                failed++;
            } else {
                bank -= num;
                cash += num;
                failed = 0;
            }
        }
    }
    
    printf("%.02f\n", bank);
    printf("%.02f", cash);

    return 0;
}