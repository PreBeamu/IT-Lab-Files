
import java.util.Scanner;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author prebe
 */
public class Save {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int total = 0;
        int count = 0;

        while (total < 1000) {
            System.out.print("Enter deposit amount: ");
            total += scan.nextInt();
            count++;
        }
        System.out.println("");
        System.out.println("Target reached!");
        System.out.println("Total amount saved = " + total);
        System.out.println("Number of deposits = " + count);
    }
}
