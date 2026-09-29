#include <stdio.h>

double celsiusToFahrenheit(double celcius);
double fahrenheitToCelcius(double fahrenheit);
void printFarenheit(double fahrenheit);
void printCelcius(double celcius);

int main() {
    double temp;
    char unit;

    scanf("%lf %c", &temp, &unit);

    if (unit == 'c' || unit == 'C') {
        double f = celsiusToFahrenheit(temp);
        printFarenheit(f);
    } else if (unit == 'f' || unit == 'F') {
        double c = fahrenheitToCelcius(temp);
        printCelcius(c);
    }

    return 0;
}

double celsiusToFahrenheit(double celcius) {
    return 32.0 + (celcius * (180.0 / 100.0));
}

double fahrenheitToCelcius(double fahrenheit) {
    return (fahrenheit - 32.0) * (100.0 / 180.0);
}

void printFarenheit(double fahrenheit) {
    printf("%.2f f\n", fahrenheit);
}

void printCelcius(double celcius) {
    printf("%.2f c\n", celcius);
}