

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author prebe
 */
public class Customer_Array {
    private String firstName;
    private String lastName;
    private Account acct[];
    private int numOfAccount;
    
    public Customer_Array(){
        this.firstName = "";
        this.lastName = "";
        this.acct = null;
    }
    
    public Customer_Array(String firstName, String lastName){
        this.firstName = firstName;
        this.lastName = lastName;
        this.acct = new Account[5];
    }
    
    public void setFirstName(String firstName){
        this.firstName = firstName;
    }
    
    public String getFirstName(){
        return firstName;
    }
    
    public void setLastName(String lastName){
        this.lastName = lastName;
    }
    
    public String getLastName(){
        return lastName;
    }
    
    public void addAccount(Account acct){
        if (numOfAccount < this.acct.length) {
            this.acct[numOfAccount] = acct;
            numOfAccount++;
        }
    }
    
    public Account getAccount(int index){
        return acct[index];
    }
    
    public int getNumOfAccount(){
        return this.numOfAccount;
    }
    
    @Override
    public String toString(){
        if (this.acct == null){
            return(firstName+" "+lastName+" doesn’t have account.");
        }
        else{
            return(firstName+" "+lastName+" have "+this.numOfAccount+" account(s).");
        }
    }
    
    public boolean equals(Customer c){
        return (this.firstName.equals(c.getFirstName())) && (this.lastName.equals(c.getLastName()));
    }
}
