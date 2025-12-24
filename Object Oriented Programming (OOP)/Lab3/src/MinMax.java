
import java.util.Scanner;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
/**
 *
 * @author prebe
 */
public class MinMax {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        boolean hasInput = false;
        while (true) {
            System.out.print("Enter a number (-1 to stop): ");
            int input = scan.nextInt();
            if (input == -1) break;
            
            hasInput = true;
            if (input > max) max = input;
            if (input < min) min = input;
        }
        System.out.println("");
        if (hasInput) {
            System.out.println("Maximum = " + max);
            System.out.println("Minimum = " + min);
        } else {
            System.out.println("No numbers were entered.");
        }
    }
}
