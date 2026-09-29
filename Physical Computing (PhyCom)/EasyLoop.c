#include <stdio.h>

int main() {
	int n;
	scanf("%d",&n);

    int i = n;
    while(i != 0) {
        printf("%d ",i);
        if (i > 0) {
            i--;
        } else {
            i++;
        }
    }
    printf("0");

	return 0;
}