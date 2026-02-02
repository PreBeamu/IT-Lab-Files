/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change handler license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit handler template
 */

/**
 *
 * @author prebe
 */
import java.awt.*;
import javax.swing.*;

public class CalculatorSample {

    private JFrame fr;
    private JTextField ans;
    private JPanel btns;
    private JButton b1, b2, b3, b4, b5, b6, b7, b8, b9, b0;
    private JButton ac, eq, o1, o2, o3, o4;

    public CalculatorSample() {
        ActionHandler handler = new ActionHandler(this);
        fr = new JFrame("My Calculator");
        ans = new JTextField();
        btns = new JPanel();

        fr.setLayout(new BorderLayout());
        fr.add(ans, BorderLayout.NORTH);
        fr.add(btns, BorderLayout.CENTER);

        // Number Buttons 0-9
        b0 = new JButton("0");
        b0.addActionListener(handler);
        b1 = new JButton("1");
        b1.addActionListener(handler);
        b2 = new JButton("2");
        b2.addActionListener(handler);
        b3 = new JButton("3");
        b3.addActionListener(handler);
        b4 = new JButton("4");
        b4.addActionListener(handler);
        b5 = new JButton("5");
        b5.addActionListener(handler);
        b6 = new JButton("6");
        b6.addActionListener(handler);
        b7 = new JButton("7");
        b7.addActionListener(handler);
        b8 = new JButton("8");
        b8.addActionListener(handler);
        b9 = new JButton("9");
        b9.addActionListener(handler);

        // Operator Buttons
        o1 = new JButton("+");
        o1.addActionListener(handler);
        o2 = new JButton("-");
        o2.addActionListener(handler);
        o3 = new JButton("x");
        o3.addActionListener(handler);
        o4 = new JButton("/");
        o4.addActionListener(handler);
        ac = new JButton("c");
        ac.addActionListener(handler);
        eq = new JButton("=");
        eq.addActionListener(handler);

        btns.setLayout(new GridLayout(4, 4));
        // Row 1
        btns.add(b7);
        btns.add(b8);
        btns.add(b9);
        btns.add(o1); // +
        // Row 2
        btns.add(b4);
        btns.add(b5);
        btns.add(b6);
        btns.add(o2); // -
        // Row 3
        btns.add(b1);
        btns.add(b2);
        btns.add(b3);
        btns.add(o3); // x
        // Row 4
        btns.add(b0);
        btns.add(ac); // c
        btns.add(eq); // =
        btns.add(o4); // /

        fr.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        fr.setSize(225, 225);
        fr.setVisible(true);
    }

    public JTextField getTextField() {
        return ans;
    }
}
