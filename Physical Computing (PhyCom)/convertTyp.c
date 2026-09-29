#include <stdio.h>

int main() {
	int num;
	scanf("%d", &num);
	float deci;
	scanf("%f", &deci);
	char charac;
	scanf(" %c", &charac);

	printf("%.03f\n",(float) num);
	printf("%d\n",(int) deci);
	printf("%d\n",(int) charac);

	return 0;
}
