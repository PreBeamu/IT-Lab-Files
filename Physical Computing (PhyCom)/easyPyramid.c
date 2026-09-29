#include <stdio.h>

int main() {
	int n;
	scanf("%d",&n);

	int star = 1;
	int spaces = n-1;
	for (int i=1; i<=n; i++) {
	    
		for (int s=1; s<=spaces; s++) {
			printf(" ");
		}
		for (int s=1; s<=star; s++) {
			printf("*");
		}
		printf("\n");
		
		star += 2;
		spaces--;
	}

	return 0;
}