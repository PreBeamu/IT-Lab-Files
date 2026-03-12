import javax.swing.*;
import javax.swing.border.*;
import java.awt.*;
import java.awt.event.*;
import java.util.*;

public class LevelSelect extends JFrame {

    private final Font loadedFont = CustomFontLoader.loadCustomFont("Jersey10.ttf");

    public LevelSelect() {
        setTitle("Level Selection");
        setSize(800, 600);
        setLayout(new BorderLayout());
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);

        add(topPanel(), BorderLayout.NORTH);
    }

    private JPanel topPanel() {
        JPanel topPanel = new JPanel(new BorderLayout());
        JButton backBtn = new BackBtn();
        JPanel moneyDisplay = new MoneyDisplay();

        topPanel.setBorder(new EmptyBorder(0, 0, 0, 75));

        topPanel.add(backBtn, BorderLayout.WEST);
        topPanel.add(moneyDisplay, BorderLayout.EAST);
        return topPanel;
    }
}