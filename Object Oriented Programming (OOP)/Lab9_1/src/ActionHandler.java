/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author prebe
 */
import java.awt.event.*;
import java.awt.*;
import javax.swing.*;

public class ActionHandler implements ActionListener, MouseListener {

    private final CalculatorSample gui;
    private int first_num;
    private int second_num;
    private String operator = null;

    public ActionHandler(CalculatorSample gui) {
        this.gui = gui;
    }

    @Override
    public void actionPerformed(ActionEvent ev) {
        String command = ev.getActionCommand();
        if ("+-x/".contains(command)) {
            gui.getTextField().setText("");
            this.operator = command;
        } else if ("0123456789".contains(command)) {
            String currentText = gui.getTextField().getText();
            gui.getTextField().setText(currentText + command);
            int newNum = Integer.parseInt(gui.getTextField().getText());
            if (this.operator == null) {
                this.first_num = newNum;
            } else {
                this.second_num = newNum;
            }
        } else if (command.equals("c")) {
            gui.getTextField().setText("");
            this.first_num = 0;
            this.second_num = 0;
            this.operator = null;
        } else if (command.equals("=")) {
            if (this.operator == null) {
                gui.getTextField().setText(this.first_num + "");
            } else {
                String result = "";
                switch (this.operator) {
                    case "+" -> result = (this.first_num + this.second_num)+"";
                    case "-" -> result = (this.first_num - this.second_num)+"";
                    case "x" -> result = (this.first_num * this.second_num)+"";
                    case "/" -> result = (this.first_num / this.second_num)+"";
                    default -> {
                    }
                }
                this.first_num = Integer.parseInt(result);
                this.second_num = 0;
                this.operator = null;
                gui.getTextField().setText(result);
            }
        }
    }
    
    @Override
    public void mouseEntered(MouseEvent e) {
        Object source = e.getSource();
        if (source instanceof JButton button) {
            button.setBackground(Color.YELLOW);
        }
    }

    @Override
    public void mouseExited(MouseEvent e) {
        Object source = e.getSource();
        if (source instanceof JButton button) {
            button.setBackground(null);
        }
    }

    @Override public void mouseClicked(MouseEvent e) {}
    @Override public void mousePressed(MouseEvent e) {}
    @Override public void mouseReleased(MouseEvent e) {}
}
