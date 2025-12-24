/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Bank;

/**
 *
 * @author prebe
 */
public class Account {
    public double balance;
    public String name;
    
    public void deposit(double b) {
        if (b < 0) {
            System.out.println("The balance variable must be greater than or equal to zero.");
        } else {
            balance += b;
        }
    }
    
    public double withdraw(double b) {
        if (balance-b < 0) {
            System.out.println("Your account balance is insufficient.");
        }
        if (b < 0) {
            System.out.println("The balance variable must be greater than or equal to zero.");
        }
        if (b >= 0 && balance-b >= 0) {
            balance -= b;
            return b;
        }
        return 0;
    }
    
    public void showInfo() {
        System.out.println("In "+name+" account, there is a balance equal to "+balance+" baht. ");
    }
}
