/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author prebe
 */
public abstract class Houses {
    private String name;
    private String color;

    public String getName() {
        return name;
    }

    public String getColor() {
        return color;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setColor(String color) {
        this.color = color;
    }
    
    public Houses() {
        this.name = "";
        this.color = "";
    }
    
    public Houses(String name, String color) {
        this.name = name;
        this.color = color;
    }

    @Override
    public String toString() {
        return "[House] : "+this.name+" , Color : "+this.color;
    }
    
    
}
