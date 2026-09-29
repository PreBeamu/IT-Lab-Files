#include <stdio.h>

int main() {
	char fname[31];
	char lname[31];
	char stuid[9];
	int d, m, y;
	float gpa;

	scanf("%30s",&fname);
	scanf("%30s",&lname);
	scanf("%8s",&stuid);
	scanf("%d/%d/%d",&d,&m,&y);
	scanf("%f",&gpa);
	
	printf("Fullname: %s %s\n",fname,lname);
	printf("ID: %s\n",stuid);
	printf("DOB: %02d-%02d-%04d\n",d,m,y);
	printf("GPA: %.2f",gpa);
	return 0;
}
