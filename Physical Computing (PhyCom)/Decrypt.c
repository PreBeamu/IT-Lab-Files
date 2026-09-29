#include <stdio.h>

int main() {
	char up_circle[] = {
		'Q', 'R', 'M', 'N', 'C', 'E', 'D', 'K', 'L', 'J',
		'O', 'S', 'H', 'T', 'U', 'F', 'V', 'Z', 'G', 'W',
		'I', 'A', 'B', 'X', 'Y', 'P'
	};
	char low_circle[] = {
		'q', 'r', 'm', 'n', 'c', 'e', 'd', 'k', 'l', 'j',
		'o', 's', 'h', 't', 'u', 'f', 'v', 'z', 'g', 'w',
		'i', 'a', 'b', 'x', 'y', 'p'
	};

	char str[201];
	scanf("%200[^\n]", str);

	int str_size = 0;
	for(int i = 0; i <= 200; i++) {
		if (str[i] == '\0') {
			str_size = i;
			break;
		}
	}

	for(int i = 0; i <= str_size; i++) {
		if (str[i] == ' ') {
			printf("%c", str[i]);
			continue;
		}
		for(int j = 0; j < 26; j++) {
			if (low_circle[j]==str[i]) {
				printf("%c", low_circle[(j + 5 + 26) % 26]);
			}
			if (up_circle[j]==str[i]) {
				printf("%c", up_circle[(j + 5 + 26) % 26]);
			}
		}
	}

	return 0;
}