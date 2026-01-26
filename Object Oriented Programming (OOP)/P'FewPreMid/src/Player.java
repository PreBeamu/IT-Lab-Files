
import java.util.Objects;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author prebe
 */
public class Player {

    private final String name;
    private final int attackDamage = 2;
    private Houses houses;
    private int hp = 20;
    private int mana = 50;

    public Player(String name) {
        this.name = name;
    }

    public Player(String name, int hp) {
        this.name = name;
        this.hp = hp;
    }

    public void setHouses(Houses houses) {
        this.houses = houses;
    }

    public void setHp(int hp) {
        if (hp > 0) {
            this.hp = hp;
            if (hp > 20) {
                this.hp = 20;
            }
        } else {
            this.hp = 0;
        }
    }

    public void setMana(int mana) {
        if (mana > 0) {
            this.mana = mana;
            if (mana > 50) {
                this.mana = 50;
            }
        } else {
            this.mana = 0;
        }
    }

    public String getName() {
        return name;
    }

    public boolean equals(Player player) {
        return (this.name.equals(player.getName()) && this.houses.equals(player.getHouses()));
    }

    public int getAttackDamage() {
        return attackDamage;
    }

    public Houses getHouses() {
        return houses;
    }

    public int getHp() {
        return hp;
    }

    public int getMana() {
        return mana;
    }

    @Override
    public String toString() {
        return "[Player] : " + this.name + " HP: " + this.hp + " Mana: " + this.mana + " || " + this.houses;
    }
    
    public void attack(Player target, Spell spell) {
        if (this.houses instanceof Magicable m) {
            m.attackSpell(this, target, spell);
        }
        if (target.getHp() <= 0) {
            System.out.println("[DEAD]: "+target.getName()+" was killed by "+this.name);
        }
    }
    
    public void protectFromPlayer(Player target){
        if (this.houses instanceof Magicable m) {
            m.defense(this,target);
        }
    }
    
}
