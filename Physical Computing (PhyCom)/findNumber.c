#include <stdio.h>

int main()
{
	double a, b, c, mid;
	scanf("%lf %lf %lf", &a, &b, &c);

	if ((a >= b && a <= c) || (a >= c && a <= b)) {
        mid = a;
    } 
    else if ((b >= a && b <= c) || (b >= c && b <= a)) {
        mid = b;
    } 
    else {
        mid = c;
    }
    
    printf("%.2f\n", mid);
	return 0;
}