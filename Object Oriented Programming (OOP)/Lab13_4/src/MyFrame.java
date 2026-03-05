import javax.swing.*;

public class MyFrame {
    public static void main(String[] args) {
        JFrame MyMainFrame = new JFrame("My Timer");
        MyTimer timerLabel = new MyTimer();
        
        Thread t = new Thread(timerLabel);
        t.start();
        
        MyMainFrame.add(timerLabel);
        MyMainFrame.setSize(350, 200);
        MyMainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        MyMainFrame.setLocationRelativeTo(null);
        MyMainFrame.setVisible(true);
    }
}