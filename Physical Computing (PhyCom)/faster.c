#include <stdio.h>

int main() {
    double fuel_price;
    scanf("%lf", &fuel_price);

    int routes[4];
    for(int i = 0; i < 4; ++i) {
        scanf("%d", &routes[i]);
    }

    double efficiencies[4];
    for(int i = 0; i < 4; ++i) {
        scanf("%lf", &efficiencies[i]);
    }

    double exp_total = 0.0;
    int exp_count = 0;
    double rom_total = 0.0;
    int rom_count = 0;

    for(int i = 0; i < 4; ++i) {
        double distance = (routes[i] == 1) ? 29.0 : 25.0;
        double toll = (routes[i] == 1) ? 60.0 : 0.0;
        
        double fuel = (efficiencies[i] > 0.0) ? (distance / efficiencies[i]) : 0.0;
        double cost = (fuel * fuel_price) + toll;
        
        printf("Day %d: fuel %.2f L, cost %.2f Baht\n", i + 1, fuel, cost);
        
        if(routes[i] == 1) {
            exp_total += cost;
            exp_count++;
        } else {
            rom_total += cost;
            rom_count++;
        }
    }

    double avg_exp = (exp_count > 0) ? (exp_total / exp_count) : 0.0;
    double avg_rom = (rom_count > 0) ? (rom_total / rom_count) : 0.0;

    printf("Expressway: %.2f Baht\n", avg_exp);
    printf("Romklao: %.2f Baht\n", avg_rom);

    return 0;
}