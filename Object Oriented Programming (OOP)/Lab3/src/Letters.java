
import java.util.Scanner;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
/**
 *
 * @author prebe
 */
public class Letters {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String word = "", conso = "";
        while (true) {
            System.out.print("Enter a character: ");
            char input = scan.next().charAt(0);
            if (input == 'z') {
                break;
            }
            if (input >= 'a' && input <= 'z') {
                word += input;
                if (input != 'a' && input != 'e' && input != 'i' && input != 'o' && input != 'u') {
                    conso += input;
                }
            } else {
                System.out.println("Invalid input. Only lowercase a-z are allowed.");
            }
        }
        System.out.println("");
        System.out.println("All characters entered: " + word);
        System.out.println("Consonants only: " + conso);
    }
}
