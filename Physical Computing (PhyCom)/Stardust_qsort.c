#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int cmp(const void *vp, const void * vq);

int main() {
    int x;
    scanf("%d", &x);

    double nums[x];
    double sum = 0, avg, median, sd;
    for (int i=0; i<x; i++) {
        scanf("%lf", &nums[i]);
        sum += nums[i];
    }
    qsort(nums, x, sizeof(double), cmp);

    avg = sum/x;
    if (x%2 != 0) {
        median = nums[x/2];
    } else {
        median = (nums[x/2]+nums[(x/2)-1])/2.0;
    }

    double zigmah = 0;
    for (int i=0; i<x; i++) {
        zigmah += pow(nums[i]-avg,2);
    }
    sd = sqrt(zigmah/x);

    printf("%.02f\n", avg);
    printf("%.02f\n", median);
    printf("%.02f\n", sd);

    return 0;
}

int cmp(const void *vp, const void *vq) {
    const double *p = vp;
    const double *q = vq;
    double diff = *p-*q;
    return ((diff >= 0.0) ? ((diff > 0.0) ? -1 : 0) : +1);
}