#include <stdio.h>
#include <math.h>

int match_name(const char *s1, const char *s2) {
    while (*s1 && *s2) {
        if (*s1 != *s2) return 0;
        s1++;
        s2++;
    }
    return *s1 == *s2;
}

int main() {
    int n;
    scanf("%d", &n);

    char names[3][20];
    scanf("%s %s %s", names[0], names[1], names[2]);

    double fuel[3] = {0.0, 0.0, 0.0};
    
    for(int i = 0; i < n; ++i) {
        double f1, f2, f3;
        scanf("%lf %lf %lf", &f1, &f2, &f3);
        fuel[0] += f1;
        fuel[1] += f2;
        fuel[2] += f3;
    }

    for(int i = 0; i < 3; ++i) {
        double capacity = 5.5;
        if(match_name(names[i], "Nano")) {
            capacity = 6.6;
        }
        
        int refills = (int)ceil(fuel[i] / capacity);
        printf("%s: %d refills\n", names[i], refills);
    }

    return 0;
}