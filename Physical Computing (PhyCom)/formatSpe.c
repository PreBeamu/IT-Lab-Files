#include <stdio.h>

int main() {
	int num;
	scanf("%d", &num);
	float deci;
	scanf("%f", &deci);
	char charac;
	scanf(" %c", &charac);
	char str[21];
	scanf("%20s", &str);

	printf("Integer: %d\n", num);
	printf("Float: %.3f\n", deci);
	printf("Character: %c\n", charac);
	printf("String: %s\n", str);
	return 0;
}
