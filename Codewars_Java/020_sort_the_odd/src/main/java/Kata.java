
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Kata {

    public static int[] sortArray(int[] array) {
        if (array.length == 0) {
            return array;
        }
        int[] result = new int[array.length];
        Arrays.fill(result, -1);
        ArrayList<Integer> odd = new ArrayList<Integer>();

        for (int i = 0; i < array.length; i++) {
            if (array[i] % 2 == 0) {
                result[i] = array[i];
            } else {
                odd.add(array[i]);
            }
        }

        Collections.sort(odd);

        for (int i = 0; i < array.length; i++) {
            if (result[i] == -1) {
                result[i] = odd.get(0);
                odd.remove(0);
            }
        }
        return result;
    }

    public static void main(String args[]) {
        int[] array1 = {5, 3, 2, 8, 1, 4};
        int[] array2 = {5, 3, 1, 8, 0};
        int[] array3 = {63, 98, 18, 50, 84, 81, 90, 18, 64, 80, 82, 20, 72, 92, 0, 0, 76, 70, 10, 38, 76};
        System.out.println(Arrays.toString(sortArray(array1)));
        System.out.println(Arrays.toString(sortArray(array2)));
        System.out.println(Arrays.toString(sortArray(array3)));

    }
}
