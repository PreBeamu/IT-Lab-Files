

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */


/**
 *
 * @author prebe
 */
public abstract class Vehicle implements Dieselable {
    protected double fuel;
    
    public Vehicle() {
        this.fuel = 0.0;
    }

    public double getFuel() {
        return fuel;
    }

    public void setFuel(double fuel) {
        this.fuel = fuel;
    }
    
    public Vehicle(double fuel) {
        this.fuel = fuel;
    }
    
    public void addFuel(double fuel) {
        this.fuel += fuel;
    }
    
    public abstract void honk();
}
