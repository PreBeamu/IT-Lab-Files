
import java.awt.event.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.io.*;

public class ActionHandler implements ActionListener, WindowListener {

    private final StudentView gui;
    private Student student;

    public ActionHandler(StudentView gui) {
        this.gui = gui;
    }

    public void loadData() {
        File file = new File("StudentM.dat");
        if (file.exists()) {
            try (FileInputStream fin = new FileInputStream(file); ObjectInputStream in = new ObjectInputStream(fin)) {
                student = (Student) in.readObject();
                gui.getName_field().setText(student.getName());
                gui.getId_field().setText(student.getID()+"");
                gui.getMoney_field().setText(student.getMoney()+"");
            } catch (IOException i) {
                i.printStackTrace();
            } catch (ClassNotFoundException c) {
                c.printStackTrace();
            }
        }
    }

    @Override
    public void actionPerformed(ActionEvent ev) {
        String command = ev.getActionCommand();
        if (command.equals("Deposit")) {
            int current_money = Integer.parseInt(gui.getMoney_field().getText());
            gui.getMoney_field().setText((current_money + 100)+"");
        } else if (command.equals("Withdraw")) {
            int current_money = Integer.parseInt(gui.getMoney_field().getText());
            gui.getMoney_field().setText((current_money - 100)+"");
        }
    }

    @Override
    public void windowOpened(WindowEvent e) {
    }

    @Override
    public void windowClosing(WindowEvent e) {
        Student student = new Student();
        student.setName(gui.getName_field().getText());
        student.setID(Integer.parseInt(gui.getId_field().getText()));
        student.setMoney(Integer.parseInt(gui.getMoney_field().getText()));
        try (FileOutputStream fOut = new FileOutputStream("StudentM.dat"); ObjectOutputStream oout = new ObjectOutputStream(fOut)) {
            oout.writeObject(student);
            System.out.println("Serialized data is saved");
        } catch (IOException i) {
            i.printStackTrace();
        }
    }

    @Override
    public void windowClosed(WindowEvent e) {
    }

    @Override
    public void windowIconified(WindowEvent e) {
    }

    @Override
    public void windowDeiconified(WindowEvent e) {
    }

    @Override
    public void windowActivated(WindowEvent e) {
    }

    @Override
    public void windowDeactivated(WindowEvent e) {
    }
}
