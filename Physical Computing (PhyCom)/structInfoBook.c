#include <stdio.h>
#include <string.h>

struct student_info {
    char name[61];
    char surname[61];
    char sex[10];
    int age;
    char id[13];
    float gpa;
};

int main() {
    struct student_info student;

    scanf("%s %s %s %d %s %f", 
          student.name, 
          student.surname, 
          student.sex, 
          &student.age, 
          student.id, 
          &student.gpa);

    char title[5];
    if (strcmp(student.sex, "Male") == 0) {
        strcpy(title, "Mr");
    } else {
        strcpy(title, "Miss");
    }

    printf("%s %c %s (%d) ID: %s GPA %.2f\n", 
           title, 
           student.name[0], 
           student.surname, 
           student.age, 
           student.id, 
           student.gpa);

    return 0;
}