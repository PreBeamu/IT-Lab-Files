import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Poring extends JFrame {
    private JLabel PoringLabel;
    private JLabel CountLabel;
    
    public Poring(int poringCount) {
        this.setResizable(false);
        this.setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);
        this.setLayout(new FlowLayout());

        ImageIcon poringIcon = new ImageIcon(getClass().getResource("/RO_Poring2916.png"));
        PoringLabel = new JLabel(poringIcon);
        CountLabel = new JLabel("" + poringCount);
        
        PoringLabel.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                dispose();
            }
        });

        this.add(PoringLabel);
        this.add(CountLabel);
        
        this.pack();
        this.setVisible(true);
    }
}