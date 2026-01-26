/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author prebe
 */
public class Gryffindor extends Houses implements Magicable {

    public Gryffindor() {
        super("Gryffindor", "RED");
    }

    @Override
    public void attackSpell(Player player, Player target, Spell spell) {
        target.setHp(target.getHp() - (spell.getDamage() + player.getAttackDamage()));
        if (spell instanceof Incendio) {
            player.setMana(player.getMana() - 4);
        } else if (spell instanceof Expelliarmus) {
            player.setMana(player.getMana() - 3);
        }
        System.out.println(player.getName() + ": use spell (" + spell.getName() + ")!");
    }

    @Override
    public void defense(Player player, Player damager) {
        player.setHp(player.getHp() + 3);
        player.setMana(player.getMana() + 4);
        System.out.println(player.getName()+": Episkey !");
    }

}
