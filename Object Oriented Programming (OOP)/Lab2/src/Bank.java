
import java.util.Scanner;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
/**
 *
 * @author prebe
 */
public class Bank {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Input your money: ");
        int money = scan.nextInt();
        System.out.print("Input your account type(Please type A B C or X in uppercase): ");
        String bank = scan.next();
        double rate = 0;
        switch (bank) {
            case "A":
            case "C":
                rate = 1.5;
                break;
            case "B":
                rate = 2.0;
                break;
            case "X":
                rate = 5.0;
                break;
            default:
                break;
        }
        int total = (int) (money + (money * (rate / 100)));
        System.out.println("Your total money in one year = " + total);
    }
}
