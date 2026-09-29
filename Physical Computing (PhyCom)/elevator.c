#include <stdio.h>

int main() {
    int start, end;
    scanf("%d %d", &start, &end);
    
    int height_start = 0;
    if (start > 1) {
        height_start = 6 + (4 * (start - 2));
    }
    
    int height_end = 0;
    if (end > 1) {
        height_end = 6 + (4 * (end - 2));
    }
    
    int s_total = height_end - height_start;
    
    if (s_total < 0) {
        s_total = -s_total;
    }
    
    if (s_total == 0) {
        printf("0.00\n");
        return 0;
    }

    double accel_s = (1.5 * 1.5) / (2.0 * 0.5);
    double accel_t = 1.5 / 0.5;
    
    double cruise_s = s_total - (2.0 * accel_s);
    double cruise_t = cruise_s / 1.5;
    
    printf("%.2f\n", accel_t + cruise_t + accel_t);

    return 0;
}