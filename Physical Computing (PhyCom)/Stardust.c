#include <stdio.h>
#include <math.h>

void bubbleSort(int arr[], int size) {
    int temp;
    for (int i=0; i<size; i++) {
        for (int j=0; j<size-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

int main() {
    int x;
    scanf("%d", &x);

    int nums[x];
    float sum = 0, avg, median, sd;
    for (int i=0; i<x; i++) {
        scanf("%d", &nums[i]);
        sum += nums[i];
    }
    bubbleSort(nums, x);

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