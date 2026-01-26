/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author prebe
 */
public abstract class Spell {
    private final String name;
    private int damage;
    
    public Spell(){
        this.name = "";
        this.damage = 0;
    }

    public Spell(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setDamage(int damage) {
        this.damage = damage;
    }

    public int getDamage() {
        return damage;
    }
}
