

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */


/**
 *
 * @author prebe
 */
public class Ship extends Vehicle implements Floatable {
    public Ship(){
        super();
    }
    
    public Ship(double fuel){
        super(fuel);
    }

    @Override
    public void honk() {
        System.out.println("Shhhhh");
    }

    @Override
    public void startEngine() {
        if (this.fuel >= 10) {
            this.fuel -= 10;
            System.out.println("Engine starts");
        }
        else {
            System.out.println("Fuel is not enough.");
        }
    }

    @Override
    public void stopEngine() {
        System.out.println("Engine stops");
    }

    @Override
    public void fl0at() {
        if (this.fuel >= 50) {
            this.fuel -= 50;
            System.out.println("Ship moves");
        }
        else {
            System.out.println("Fuel is not enough.");
        }
    }
    
    public void move() {
        this.fl0at();
    }
    
    public void move(int distance) {
        for (int i = 0; i < distance; i++){
            if (this.fuel < 50) {
                System.out.println("Fuel is not enough.");
                break;
            }
            else {
                this.fl0at();
            }
        }
    }
}
