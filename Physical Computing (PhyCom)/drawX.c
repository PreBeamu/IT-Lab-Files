#include <stdio.h>

int main()
{
	int n = 0;
	scanf("%d",&n);

	int dash_f = 1,dash_b = n;
	for (int i=1; i<=n; i++) {
		for (int x=1; x<=n; x++) {
			if (x == dash_f || x == dash_b) {
				printf("-");
			} else {
				printf("#");
			}
		}
		printf("\n");
		dash_f++;
		dash_b--;
	}

	return 0;
}