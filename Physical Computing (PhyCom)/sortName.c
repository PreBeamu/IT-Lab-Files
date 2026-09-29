#include <stdio.h>

int main() {
    char names[20][65];
    int i, j, k;

    for (i = 0; i < 20; i++) {
        scanf(" %[^\n]", names[i]);
        
        int newWord = 1;
        for (j = 0; names[i][j] != '\0'; j++) {
            if (names[i][j] == ' ') {
                newWord = 1;
            } else if (newWord) {
                if (names[i][j] >= 'a' && names[i][j] <= 'z') {
                    names[i][j] -= 32; 
                }
                newWord = 0;
            } else {
                if (names[i][j] >= 'A' && names[i][j] <= 'Z') {
                    names[i][j] += 32;
                }
            }
        }
    }

    for (i = 0; i < 19; i++) {
        for (j = 0; j < 19 - i; j++) {
            
            int cmp = 0;
            for (k = 0; names[j][k] != '\0' || names[j+1][k] != '\0'; k++) {
                if (names[j][k] != names[j+1][k]) {
                    cmp = names[j][k] - names[j+1][k];
                    break;
                }
            }
            
            if (cmp > 0) {
                char temp;
                for (k = 0; k < 65; k++) {
                    temp = names[j][k];
                    names[j][k] = names[j+1][k];
                    names[j+1][k] = temp;
                    
                    if (names[j][k] == '\0' && names[j+1][k] == '\0') {
                        break; 
                    }
                }
            }
        }
    }

    for (i = 0; i < 20; i++) {
        printf("%s\n", names[i]);
    }

    return 0;
}