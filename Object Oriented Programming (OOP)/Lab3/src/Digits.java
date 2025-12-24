
import java.util.Scanner;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
/**
 *
 * @author prebe
 */
public class Digits {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter number of digits: ");
        int n = scan.nextInt();
        String num = "";
        for (int i = 1; i <= n; i++) {
            System.out.print("Enter digit " + i + ": ");
            num += scan.next();
        }
        System.out.println("");
        System.out.println("Final Code = "+num);
    }
}
