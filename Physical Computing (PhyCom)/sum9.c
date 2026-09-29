#include <stdio.h>

int main()
{
	int sum = 0, lin;
	while (1) {
		int x;
		scanf("%d",&x);
		if (x == -9) {
		    break;
		}
		sum += x;
		lin = x;
	}
	printf("%d", sum);

	return 0;
}