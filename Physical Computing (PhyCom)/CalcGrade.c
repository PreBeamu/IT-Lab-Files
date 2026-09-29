#include <stdio.h>

int main(){
	char name[40];
	scanf("%[^\n]", &name);
	int g1,g2,g3,g4,g5,g6;
	scanf("%d %d %d %d %d %d",&g1,&g2,&g3,&g4,&g5,&g6);
	float avg = (float) (g1+g2+g3+g4+g5+g6)/6;

	printf("Grade announcement 1/2568: %s\n", name);
	printf("GPS/GPA: %0.2f", avg);
	return 0;
}
