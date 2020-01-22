import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

/**
 * Custom simulator of rolling dices.
 *
 * @author Przemyslaw Perzyna
 * @version 0.1
 */
public class Dice
{
    public Dice(int size)
    {}

    public static int diceRoll (int diceSize) {
        //return a number from range <1 : diceSize>
        //both ends are included
        Random r = new Random ();
        int result = 1+r.nextInt(diceSize);

        return result;
    }

    public static void main(String args[]) {
        System.out.println("Hello to my DiceRollSimulator \n");
        String in = "";
        boolean repeat = true;
        ArrayList<Integer> rollHistory = new ArrayList<Integer>();

        while(repeat) {
            System.out.println("-----------------------------"); 
            System.out.println("Please enter dice size");
            System.out.println("(if you want to exit type 'exit')");            
     
            in = System.console().readLine();               

            if (in.matches("\\d+") && Integer.parseInt(in)>1) {
                System.out.println("Your input is a viable dice size");
                int result = Dice.diceRoll(Integer.parseInt(in));
                rollHistory.add(result);
                System.out.println("Your roll is: "+result);
            }
            else {
                System.out.println("Your input is not a viable dice size");
                System.out.println("Please enter a integer greater than 1");
                if (in.equals("exit")) {
                    System.out.println("You have entered 'exit'");
                    repeat = false;}                
            }

        }

        System.out.println("Exiting program...\n");

        System.out.println("Press 'y' to see list of your rolls");
        System.out.println("Or any other key to exit");
        in = System.console().readLine();  
        if (in.equals("y")) {
        System.out.println("List of rolls: "+Arrays.toString(rollHistory.toArray()));
        }
    }
}
