
import java.util.Scanner;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
/**
 *
 * @author prebe
 */
public class GradeCheck {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter GPA: ");
        double grade = scan.nextDouble();
        System.out.print("Enter family income: ");
        int income = scan.nextInt();
        if (grade < 3.5) {
            System.out.println("You are not eligible for a scholarship.");
        } else {
            if (income > 15_000) {
                System.out.println("You are not eligible for a scholarship.");
            } else {
                System.out.println("You are eligible for a scholarship.");
            }
        }
    }
}
