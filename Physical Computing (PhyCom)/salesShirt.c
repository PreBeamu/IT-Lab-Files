#include <stdio.h>

int main() {
    double price, discount, amount;
    double net_price;
    
    scanf("%lf", &price);
    scanf("%lf", &discount);
    scanf("%lf", &amount);
    
    net_price = (price - (price * (discount / 100.0))) * amount;
    
    printf("%.2f\n", net_price);
    
    return 0;
}