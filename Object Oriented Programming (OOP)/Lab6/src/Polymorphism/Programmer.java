/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Polymorphism;

/**
 *
 * @author prebe
 */
public class Programmer extends Employee {

    private int happiness;

    public void coding(String str) {
        if (getEnergy() >= 30) {
            System.out.println("Your code is " + str);
            setEnergy(getEnergy() - 30);
            setHappiness(getHappiness() - 30);
        } else {
            System.out.println("Error Error Error");
            setEnergy(getEnergy() - 30);
            setHappiness(getHappiness() - 30);
        }
    }

    public void coding(char str) {
        this.coding(str+"");
    }

    public void setHappiness(int happiness) {
        this.happiness = happiness;
    }

    public int getHappiness() {
        return this.happiness;
    }
}
