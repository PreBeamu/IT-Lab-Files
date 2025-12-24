
import java.util.Scanner;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
/**
 *
 * @author prebe
 */
public class Tax {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter your salary: ");
        double salary = scan.nextDouble();
        if (salary > 50_000) {
            System.out.print("You tax is: " + (salary * 0.1));
        } else {
            System.out.print("You tax is: " + (salary * 0.05));
        }
    }
}
