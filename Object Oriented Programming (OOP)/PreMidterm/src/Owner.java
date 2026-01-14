/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author prebe
 */
public class Owner {

    protected final String name;
    protected Animal animal;

    public Owner() {
        this.name = "";
        this.animal = null;
    }

    public Owner(String name) {
        this.name = name;
        this.animal = null;
    }

    public Owner(Animal animal) {
        this.name = "";
        this.animal = animal;
    }

    public Owner(String name, Animal animal) {
        this.name = name;
        this.animal = animal;
    }

    public String getName() {
        return this.name;
    }

    public void setAnimal(Animal animal) {
        this.animal = animal;
    }

    public Animal getAnimal() {
        return this.animal;
    }

    public void feedFood(Food f) {
        this.animal.eat(f);
    }
    
    @Override
    public String toString() {
        return "Owner name = " + name + ", " + animal.toString();
    }
    
    public void protectOwnerFrom(Animal a) {
        if (this.animal instanceof Dog my_a) {
            my_a.kick(a);
        } else if (this.animal instanceof Pigeous my_a) {
            my_a.wingAttack(a);
        }
    }
}
