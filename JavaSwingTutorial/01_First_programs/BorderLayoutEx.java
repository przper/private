import javax.swing.JFrame;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.BorderLayout;
import java.awt.EventQueue;

public class BorderLayoutEx extends JFrame
{
    private JButton button;
    private JTextArea textArea;
    
    
    public BorderLayoutEx()
    {
        super("Hello World"); //calling parent class constructor
        
        setLayout(new BorderLayout());
        
        button = new JButton("Click me");
        textArea = new JTextArea();
        
        button.addActionListener((event) -> textArea.append("Hello\n"));
        
        add(textArea,BorderLayout.CENTER);
        add(button, BorderLayout.SOUTH);
        
        setSize(600,600);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setVisible(true);
    }


    public static void main (String args[]){
            EventQueue.invokeLater(() -> {
                var ex = new BorderLayoutEx();
            });
    }
}
