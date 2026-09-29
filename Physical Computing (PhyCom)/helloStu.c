#include <stdio.h>

int main() {
	char fname[21], sname[21];
	scanf("%20s %20s",&fname, &sname);
	char nick[21];
	scanf("%20s",&nick);
	char id[9];
	scanf("%8s", id);

	printf("Hello World, my name is %s (%s)\n", nick, fname);
	printf("\n");
	printf("Student ID: %s\n", id);
	printf("Name: %s %s\n", fname, sname);
	printf("Nickname: %s", nick);

	return 0;
}
