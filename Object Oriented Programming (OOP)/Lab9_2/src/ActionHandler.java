/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author prebe
 */
import java.awt.event.*;

public class ActionHandler implements ActionListener {

    private final TellerGUI gui;
    private final Account account;

    public ActionHandler(TellerGUI gui) {
        this.gui = gui;
        this.account = new Account();
        this.account.balance = 6000;
    }

    @Override
    public void actionPerformed(ActionEvent ev) {
        String command = ev.getActionCommand();
        String inputText = gui.getAmtInput().getText().trim();

        if (command.equals("Exit")) {
            System.exit(0);
        }

        if (!inputText.isEmpty()) {
            double amount = Double.parseDouble(inputText);
            if (command.equals("Withdraw")) {
                account.withdraw(amount);
            } else if (command.equals("Deposit")) {
                account.deposit(amount);
            }
            gui.getBalanceValue().setText(account.balance + "");
        }
    }
}
