
import java.util.Scanner;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author prebe
 */
public class Students {
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter number of students: ");
        int n = scan.nextInt();
        int ex = 0, go = 0, fa = 0, po = 0;
        for (int i = 1; i <= n; i++) {
            System.out.print("Enter score for student " + i + ": ");
            int score = scan.nextInt();
            if (score >= 80) {
                System.out.println("Excellent");
                ex += 1;
            } else if (score >= 60 && score <= 79) {
                System.out.println("Good");
                go += 1;
            } else if (score >= 50 && score <= 59) {
                System.out.println("Fair");
                fa += 1;
            } else {
                System.out.println("Poor");
                po += 1;
            }    
        }
        System.out.println("");
        System.out.println("Summary:");
        System.out.println("Excellent: "+ex);
        System.out.println("Good: "+go);
        System.out.println("Fair: "+fa);
        System.out.println("Poor: "+po);
    }
}
