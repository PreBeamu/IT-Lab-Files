
import java.awt.*;
import javax.swing.*;

public class ChatDemo {

    ActionHandler handler = new ActionHandler(this);
    private JFrame fr;
    private JTextArea chatbox;
    private JPanel interact, btns;
    private JTextField msg;
    private JButton sub, res;

    public ChatDemo() {
        fr = new JFrame();
        chatbox = new JTextArea(20, 45);
        interact = new JPanel();
        btns = new JPanel();
        msg = new JTextField();
        sub = new JButton("Submit");
        res = new JButton("Reset");
        handler.loadChatHistory();

        chatbox.setEditable(false);
        fr.setLayout(new BorderLayout());
        fr.add(chatbox, BorderLayout.CENTER);
        fr.addWindowListener(handler);

        interact.setLayout(new GridLayout(2, 1));
        interact.add(msg);
        interact.add(btns);
        btns.add(sub);
        btns.add(res);
        fr.add(interact, BorderLayout.SOUTH);

        sub.addActionListener(handler);
        res.addActionListener(handler);

        fr.pack();
        fr.setVisible(true);
        fr.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    public JTextField getMsgBox() {
        return msg;
    }

    public JTextArea getChatBox() {
        return chatbox;
    }
}
