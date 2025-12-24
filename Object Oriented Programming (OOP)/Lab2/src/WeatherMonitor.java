
import java.util.Scanner;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author prebe
 */
public class WeatherMonitor {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter temperature (°C): ");
        double temperature = scanner.nextDouble();
        System.out.print("Enter humidity (%): ");
        double humidity = scanner.nextDouble();
        System.out.println(); 
        if (temperature > 37.5) {
            System.out.println("Warning: High temperature!");
        } else {
            System.out.println("Temperature normal.");
        }
        if (humidity > 80) {
            System.out.println("Humidity is too high.");
        } else {
            System.out.println("Humidity is acceptable.");
        }
    }
}
