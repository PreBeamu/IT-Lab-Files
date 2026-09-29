#include <stdio.h>

double findMin(double array[], int size);
double findMax(double array[], int size);
double findAvg(double array[], int size);
double getValue();

int main() {
    int n;
    scanf("%d", &n);

    double array[n];
    for (int i=0; i<n; ++i) {
        array[i] = getValue();
    }

    double min, max, avg;
    min = findMin(array, n);
    max = findMax(array, n);
    avg = findAvg(array, n);

    printf("%d Values\n", n);
    printf("Min: %.03f\n", min);
    printf("Max: %.03f\n", max);
    printf("Avg: %.03f\n", avg);

    return 0;
}

double getValue() {
    double value;
    scanf("%lf", &value);
    return value;
}

double findMin(double array[], int size) {
    double min = array[0];
    for (int i=0; i<size; ++i) {
        if (array[i] < min) {
            min = array[i];
        }
    }
    return min;
}

double findMax(double array[], int size) {
    double max = array[0];
    for (int i=0; i<size; ++i) {
        if (array[i] > max) {
            max = array[i];
        }
    }
    return max;
}

double findAvg(double array[], int size) {
    double avg = 0;
    for (int i=0; i<size; ++i) {
        avg += array[i];
    }
    return avg/size;
}