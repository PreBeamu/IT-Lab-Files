
import java.util.Scanner;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
/**
 *
 * @author prebe
 */
public class Items {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter number of items: ");
        int n = scan.nextInt();
        int total = 0;
        for (int i = 1; i <= n; i++) {
            System.out.print("Enter price for item " + i + ": ");
            total += scan.nextInt();
        }
        System.out.println("Total = " + total);
        System.out.println("");
        System.out.print("Enter amount paid: ");
        int paid = scan.nextInt();
        System.out.println("Change " + (paid - total));
    }
}
