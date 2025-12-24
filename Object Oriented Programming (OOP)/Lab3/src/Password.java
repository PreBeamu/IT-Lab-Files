
import java.util.Scanner;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
/**
 *
 * @author prebe
 */
public class Password {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        while (true) {
            System.out.print("Enter password: ");
            String pass = scan.next();
            if (pass.equals("PASS2025")) {
                System.out.println("Access granted.");
                break;
            } else {
                System.out.println("Try again.");
            }
        }
    }
}
