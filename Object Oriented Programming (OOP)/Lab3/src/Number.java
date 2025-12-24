
import java.util.Scanner;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
/**
 *
 * @author prebe
 */
public class Number {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int odd = 0, even = 0;
        while (true) {
            int num = scan.nextInt();
            if (num == -1) {
                break;
            } else {
                if (num%2 == 0) {
                    even += 1;
                } else {
                    odd += 1;
                }
            }
        }
        System.out.println("Odd number = "+odd+" and Even number = "+even);
    }
}
