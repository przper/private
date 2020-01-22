
import javax.swing.GroupLayout;
import javax.swing.ButtonGroup;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JRadioButton;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.EventQueue;

import static javax.swing.GroupLayout.Alignment.LEADING;
import static javax.swing.LayoutStyle.ComponentPlacement.RELATED;

public class App extends JFrame {

    public App() {

        initUI();
    }

    private void initUI() {

        var pane = getContentPane();
        var gl = new GroupLayout(pane);

        pane.setLayout(gl);
        gl.setAutoCreateContainerGaps(true);
        gl.setAutoCreateGaps(true);

        var field = new JTextField(15);;
        var rollBtn = new JButton("Roll!");
        var d2size = new JRadioButton("d2");
        var d4size = new JRadioButton("d4");
        var d6size = new JRadioButton("d6");
        var d8size = new JRadioButton("d8");
        var d10size = new JRadioButton("d10");
        var d12size = new JRadioButton("d12");
        var d20size = new JRadioButton("d20");

        var sizeGroup = new ButtonGroup();
        sizeGroup.add(d2size);
        sizeGroup.add(d4size);
        sizeGroup.add(d6size);
        sizeGroup.add(d8size);
        sizeGroup.add(d10size);
        sizeGroup.add(d12size);
        sizeGroup.add(d20size);

        gl.setHorizontalGroup(gl.createSequentialGroup()
            .addGroup(gl.createParallelGroup()
                .addComponent(d2size)
                .addComponent(d4size)
                .addComponent(d6size)
                .addComponent(d8size)
                .addComponent(d10size)
                .addComponent(d12size)
                .addComponent(d20size))
            .addGap(30)
            .addGroup(gl.createParallelGroup()
                .addComponent(field, GroupLayout.DEFAULT_SIZE, 
                GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
                .addComponent(rollBtn))
        );

        gl.setVerticalGroup(gl.createParallelGroup()
            .addGroup(gl.createSequentialGroup()
                .addComponent(d2size)
                .addComponent(d4size)
                .addComponent(d6size)
                .addComponent(d8size)
                .addComponent(d10size)
                .addComponent(d12size)
                .addComponent(d20size))
            .addGroup(gl.createSequentialGroup()
                .addComponent(field, GroupLayout.DEFAULT_SIZE, 
                GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(RELATED)
                .addComponent(rollBtn))
        );                

        pack();
        setTitle("DiceRollSimulator");
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    public static void main(String[] args) {

        EventQueue.invokeLater(() -> {
                var ex = new App();
                ex.setVisible(true);
            });
    }
}