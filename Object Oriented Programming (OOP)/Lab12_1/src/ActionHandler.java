
import java.awt.event.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.io.*;

public class ActionHandler implements ActionListener, WindowListener {

    private final ChatDemo gui;
    private String chatMsg = "";

    public ActionHandler(ChatDemo gui) {
        this.gui = gui;
    }

    public void loadChatHistory() {
        File file = new File("ChatDemo.dat");

        if (file.exists()) {
            try (FileReader fr = new FileReader(file)) {
                int ch = fr.read();
                while (ch != -1) {
                    chatMsg += (char) ch;
                    ch = fr.read();
                }
                gui.getChatBox().setText(chatMsg);
                fr.close();
            } catch (IOException ex) {
                ex.printStackTrace();
            }
        }
    }

    private void sendMsg(String txt) {
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy/MM/dd HH:mm:ss");
        String oldText = gui.getChatBox().getText();
        gui.getChatBox().setText(oldText + "  " + dtf.format(LocalDateTime.now()) + " : " + txt + "\n");
        chatMsg = gui.getChatBox().getText();
        gui.getMsgBox().setText("");
    }

    @Override
    public void actionPerformed(ActionEvent ev) {
        String command = ev.getActionCommand();
        if (command.equals("Submit")) {
            this.sendMsg(gui.getMsgBox().getText());
        } else if (command.equals("Reset")) {
            gui.getChatBox().setText("");
        }
    }

    @Override
    public void windowOpened(WindowEvent e) {
    }

    @Override
    public void windowClosing(WindowEvent e) {
        try (FileWriter fw = new FileWriter("ChatDemo.dat")) {
            for (int i = 0; i < chatMsg.length(); i++) {
                fw.write(chatMsg.charAt(i));
            }
        } catch (IOException ex) {
            System.out.print(ex);
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
