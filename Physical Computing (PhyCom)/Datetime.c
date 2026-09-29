#include <stdio.h>

int main() {
    int sec;
    scanf("%d", &sec);
    
    int days = sec / 86400;
    int hours = (sec % 86400) / 3600;
    int mins = (sec % 3600) / 60;
    int remains = sec % 60;
    printf("%d s = %d d %d h %d m %d s\n", sec, days, hours, mins, remains);
    
    return 0;
}