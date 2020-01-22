
import java.util.Arrays;

public class Kata {

    public static int[] beggars(int[] values, int n) {
        System.out.println("Array: " + Arrays.toString(values) + "; n: " + n);
        int counter = 0;
        int[] result = new int[n];
        if (n != 0) {
            for (int v : values) {
                System.out.println("Value: " + v + "; counter: " + counter);
                result[counter] += v;
                counter++;

                if (counter == n) {
                    counter = 0;
                }
            }
        }
        System.out.println(Arrays.toString(result));
        return result;
    }

    public static void main(String args[]) {
        int[] test = {1, 2, 3, 4, 5};
        beggars(test, 0);
        //System.out.println(Arrays.toString(beggars(test, 3)));
    }
}
