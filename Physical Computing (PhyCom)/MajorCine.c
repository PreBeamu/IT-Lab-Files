#include <stdio.h>

int main() {
    int age, day, price;
    
    scanf("%d", &age);
    scanf("%d", &day);

    if (day == 4) {
        price = 100;
    } else {
        if (age <= 12) {
            price = 120;
        } else if (age >= 60) {
            price = 140;
        } else {
            price = 220;
        }

        if (day == 1 || day == 7) {
            price += 20;
        }
    }

    printf("Ticket price: %d Baht", price);

    return 0;
}