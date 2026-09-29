#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

struct student_info {
    char name[61];
    char surname[61];
    char sex[10];
    int age;
    char id[13];
    float gpa;
};

int compare_name(const void *a, const void *b) {
    struct student_info *s1 = (struct student_info *)a;
    struct student_info *s2 = (struct student_info *)b;
    return strcmp(s1->name, s2->name);
}

int compare_surname(const void *a, const void *b) {
    struct student_info *s1 = (struct student_info *)a;
    struct student_info *s2 = (struct student_info *)b;
    return strcmp(s1->surname, s2->surname);
}

int compare_id(const void *a, const void *b) {
    struct student_info *s1 = (struct student_info *)a;
    struct student_info *s2 = (struct student_info *)b;
    return strcmp(s1->id, s2->id);
}

int main() {
    struct student_info students[20];
    char option[20];

    for (int i = 0; i < 20; i++) {
        scanf("%s %s %s %d %s %f",
              students[i].name,
              students[i].surname,
              students[i].sex,
              &students[i].age,
              students[i].id,
              &students[i].gpa);
    }

    scanf("%s", option);

    for (int i = 0; option[i] != '\0'; i++) {
        option[i] = tolower((unsigned char)option[i]);
    }

    if (strcmp(option, "name") == 0) {
        qsort(students, 20, sizeof(struct student_info), compare_name);
    } else if (strcmp(option, "surname") == 0) {
        qsort(students, 20, sizeof(struct student_info), compare_surname);
    } else if (strcmp(option, "id") == 0) {
        qsort(students, 20, sizeof(struct student_info), compare_id);
    }

    for (int i = 0; i < 20; i++) {
        char title[5];
        if (strcmp(students[i].sex, "Male") == 0) {
            strcpy(title, "Mr");
        } else {
            strcpy(title, "Miss");
        }

        printf("%s %c %s (%d) ID: %s GPA %.2f\n",
               title,
               students[i].name[0],
               students[i].surname,
               students[i].age,
               students[i].id,
               students[i].gpa);
    }

    return 0;
}