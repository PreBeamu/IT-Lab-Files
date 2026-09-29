#include <stdio.h>

int main() {
	char name[101];
	scanf("%100[^\n]", &name);
	double power;
	scanf("%lf", &power);
	double weight;
        scanf("%lf", &weight);
	double price;
        scanf("%lf", &price);

	printf("%.04f\n", power);
	printf("%.04f\n", weight);
	printf("%.02f\n", price);
	printf("%s", name);

	return 0;
}
