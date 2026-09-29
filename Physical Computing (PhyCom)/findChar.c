#include <stdio.h>

int main()
{
	char str[301] = "";
	scanf("%300[^\n]", str);

	int str_size = 0;
	for(int i = 0; i <= 300; i++) {
		if (str[i] == '\0') {
			str_size = i;
			break;
		}
	}

	char target;
	scanf(" %c", &target);

	int idx_size = 0, pos[300];
	for(int i = 0; i < str_size; i++) {
		if (str[i] == target || str[i] == target-32 || str[i] == target+32) {
			pos[idx_size] = i+1;
			idx_size++;
		}
	}

	if(idx_size <= 0) {
		printf("Not found.");
		return 0;
	}

	printf("There is/are %d \"%c\" in the above sentences.\n",idx_size,target);
	printf("Position: ");
	for(int i = 0; i < idx_size-1; i++) {
		printf("%d, ", pos[i]);
	}
	printf("%d", pos[idx_size-1]);

	return 0;
}