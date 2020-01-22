import javax.swing.JFrame;

public class SimpleEx extends JFrame
{

    public SimpleEx()
    {
        initUI();
    }

    private void initUI() {
        setTitle("My first GUI");
        setSize(300,200);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(EXIT_ON_CLOSE);    
    }

    public static void main(String args[]) {
        var ex = new SimpleEx();
        ex.setVisible(true);
    }
}