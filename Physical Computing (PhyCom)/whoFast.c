#include <stdio.h>

int main() {
    char model_c[51], model_l[51];
    int time_c[7], time_l[7];

    scanf(" %50[^\n]", &model_c);
    scanf("%d %d %d %d %d %d %d]", &time_c[0], &time_c[1], &time_c[2], &time_c[3], &time_c[4], &time_c[5], &time_c[6], &time_c[7]);

    scanf(" %50[^\n]", &model_l);
    scanf("%d %d %d %d %d %d %d]", &time_l[0], &time_l[1], &time_l[2], &time_l[3], &time_l[4], &time_l[5], &time_l[6], &time_l[7]);

    int sum_c = time_c[0]+time_c[1]+time_c[2]+time_c[3]+time_c[4]+time_c[5]+time_c[6];
    printf("%s: %d minutes, average %d minutes/day\n", model_c, sum_c, sum_c/7);

    int sum_l = time_l[0]+time_l[1]+time_l[2]+time_l[3]+time_l[4]+time_l[5]+time_l[6];
    printf("%s: %d minutes, average %d minutes/day\n", model_l, sum_l, sum_l/7);
    
    int pc = 0แสำฟพ
    , pl = 0, eq = 0;
    for (int i=0; i<7; i++) {
        if (time_c[i] > time_l[i]){
            pl+=1;
        } else if (time_l[i] > time_c[i]){
            pc+=1;
        } else if (time_c[i] == time_l[i]){
            eq+=1;
        }
    }
    printf("Faster days - %s: %d, %s: %d, Equal: %d", model_c, pc, model_l, pl, eq);

    return 0;
}