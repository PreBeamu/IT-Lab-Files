#include <stdio.h>

int main() {
    double price;
    int discount;
    int amount;

    scanf("%lf", &price);
    scanf("%d", &discount);
    scanf("%d", &amount);

    double total_promo1 = (price * (100.0 - discount) / 100.0) * amount;

    int paid_amount = amount - (amount / 3);
    double total_promo2 = paid_amount * price;

    if (total_promo1 <= total_promo2) {
        printf("Discount %d%%\n", discount);
        printf("%.2f\n", total_promo1);
    } else {
        printf("Buy 2 Get 1\n");
        printf("%.2f\n", total_promo2);
    }

    return 0;
}