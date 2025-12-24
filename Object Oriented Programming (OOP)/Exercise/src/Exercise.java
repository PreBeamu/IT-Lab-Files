
import java.util.Scanner;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author prebe
 */
public class Exercise {
    public static void main(String[] args) {
        int time1, time2;
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter your exercise time 1: ");
        time1 = scan.nextInt();
        System.out.print("Enter your exercise time 2: ");
        time2 = scan.nextInt();
        int total = time1 + time2;
        int hours = total / 3600;
        int minutes = (total % 3600) / 60;
        int seconds = total % 60;
        System.out.println("It is " + hours + " hours " + minutes + " minutes and " + seconds + " seconds.");
    }
}
