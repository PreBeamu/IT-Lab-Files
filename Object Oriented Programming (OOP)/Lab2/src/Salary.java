
import java.util.Scanner;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
/**
 *
 * @author prebe
 */
public class Salary {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Please insert your name: ");
        String name = scan.next();
        System.out.print("Please insert your age: ");
        int age = scan.nextInt();
        System.out.print("Please insert numbers of workings days: ");
        int numDay1 = scan.nextInt();
        System.out.print("Please insert numbers of absent days: ");
        int numDay2 = scan.nextInt();
        System.out.print("Please insert your body weight: ");
        int weight = scan.nextInt(), salary = 0;
        //
        if (age >= 21) {
            if (age <= 30) {
                salary = (numDay1 * 300) - (numDay2 * 50);
            } else if (age <= 40) {
                salary = (numDay1 * 500) - (numDay2 * 50);
            } else if (age <= 50) {
                salary = (numDay1 * 1000) - (numDay2 * 25);
            } else if (age <= 60) {
                salary = (numDay1 * 3000);
            } else {
                System.out.println("Grade F");
            }
        }
        //
        System.out.println("Hi, " + name);
        System.out.println("Your salary is " + salary + " Baht");
        //
        if (weight >= 10) {
            if (weight <= 60) {
                salary += 5000;
            } else if (weight <= 90) {
                salary += (5000 - ((weight - 60) * 10));
            }
        }
        //
        System.out.println("Your salary and bonus is " + salary + " Baht");
    }
}
