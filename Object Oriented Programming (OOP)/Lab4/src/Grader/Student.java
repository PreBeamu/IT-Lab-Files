/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Grader;

/**
 *
 * @author prebe
 */
public class Student {

    public String name;
    public double mScore;
    public double fScore;

    public void showGrade() {
        double s = (mScore * 0.4) + (fScore * 0.4) + 20;
        System.out.print("Your grade is ");
        if (s >= 80) {
            System.out.print('A');
        } else if (s >= 70) {
            System.out.print('B');
        } else if (s >= 60) {
            System.out.print('C');
        } else if (s >= 50) {
            System.out.print('D');
        } else if (s < 50) {
            System.out.print('F');
        }
        System.out.println(".");
    }
}
