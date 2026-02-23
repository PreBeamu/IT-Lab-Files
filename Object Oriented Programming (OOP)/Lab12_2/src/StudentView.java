
import java.awt.*;
import javax.swing.*;

public class StudentView {

    private JFrame fr;
    private JPanel id_frame, name_frame, money_frame, btns;
    private JLabel id_label, name_label, money_label;
    private JTextField id_field, name_field, money_field;
    private JButton dep, with;

    public StudentView() {
        ActionHandler handler = new ActionHandler(this);
        fr = new JFrame();
        id_frame = new JPanel();
        name_frame = new JPanel();
        money_frame = new JPanel();
        btns = new JPanel();
        id_label = new JLabel("    ID :");
        name_label = new JLabel("    Name :");
        money_label = new JLabel("    Money :");
        id_field = new JTextField();
        name_field = new JTextField();
        money_field = new JTextField("100");
        dep = new JButton("Deposit");
        with = new JButton("Withdraw");
        handler.loadData();
        
        money_field.setEditable(false);
        fr.setLayout(new GridLayout(4,1));
        fr.add(id_frame);
        fr.add(name_frame);
        fr.add(money_frame);
        fr.add(btns);
        fr.addWindowListener(handler);
        
        id_frame.setLayout(new GridLayout(1,2));
        id_frame.add(id_label);
        id_frame.add(id_field);
        
        name_frame.setLayout(new GridLayout(1,2));
        name_frame.add(name_label);
        name_frame.add(name_field);
        
        money_frame.setLayout(new GridLayout(1,2));
        money_frame.add(money_label);
        money_frame.add(money_field);
        
        btns.add(dep);
        btns.add(with);
        dep.addActionListener(handler);
        with.addActionListener(handler);

        fr.pack();
        fr.setVisible(true);
        fr.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    public JTextField getMoney_field() {
        return money_field;
    }

    public JTextField getId_field() {
        return id_field;
    }

    public JTextField getName_field() {
        return name_field;
    }
}
