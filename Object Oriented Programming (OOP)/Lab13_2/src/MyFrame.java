import javax.swing.*;
import java.awt.*;

public class MyFrame {
    public static void main(String[] args) {
        JFrame MyMainFrame = new JFrame("My Clock");
        MyClock clock = new MyClock();
        Thread t = new Thread(clock);
        
        t.start();
        
        MyMainFrame.add(clock, BorderLayout.CENTER);
        MyMainFrame.setSize(300, 150);
        MyMainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        MyMainFrame.setLocationRelativeTo(null);
        MyMainFrame.setVisible(true);
    }
}