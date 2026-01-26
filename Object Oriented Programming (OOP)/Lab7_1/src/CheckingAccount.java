

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
/**
 *
 * @author prebe
 */
public class CheckingAccount extends Account {

    private double credit;

    public CheckingAccount() {
        super(0, "");
        credit = 0;
    }

    public CheckingAccount(double balance, String name, double credit) {
        super(balance, name);
        this.credit = credit;
    }

    public void setCredit(double credit) {
        if (credit > 0) {
            this.credit = credit;
        } else {
            System.out.println("Input number must be a positive integer.");
        }
    }

    public double getCredit() {
        return credit;
    }

    @Override
    public void withdraw(double a) {
        if (a <= 0) {
            System.out.println("Input number must be a positive integer.");
        } else if (super.getBalance() >= a) {
            super.setBalance(super.getBalance() - a);
            System.out.println(a + " baht is withdrawn from " + super.name + " and your credit balance is " + credit + ".");
        } else if (super.getBalance() + credit >= a) {
            double balanceBeforeUpdate = super.getBalance();
            double amountToExtractFromCredit = a - balanceBeforeUpdate;

            super.setBalance(0);
            this.credit = this.credit - amountToExtractFromCredit;

            System.out.println(a + " baht is withdrawn from " + super.name + " and your credit balance is " + credit + ".");
        } else {
            System.out.println("Not enough money!");
        }
    }

    public void withdraw(String a) {
        double result;
        result = Double.parseDouble(a);
        withdraw(result);
    }

    @Override
    public String toString() {
        return "The " + super.name + " account has " + super.balance + " baht and " + credit + " credits.";
    }
}
