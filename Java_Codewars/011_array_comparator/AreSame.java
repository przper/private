import java.util.Arrays;

public class AreSame {

    public static boolean comp(int[] a, int[] b) {
        Integer[] square = new Integer[a.length];
        boolean result = true;
        boolean isIn = false;
        for (int i=0;i<a.length;i++) {
            square[i]=a[i]*a[i];
        }
        System.out.println(Arrays.toString(a));
        System.out.println(Arrays.toString(square));

        for (int number : b) {
            for (int num : square) {
                if (num == number) {
                    isIn = true;
                    break;
                }
                
            }
        }
        return result;
    }

    public static boolean contains(int[] array, int v) {
        boolean result = false;
        for (int i:array) {
            if (i==v) {
                result = true;
                break;
            }
        }
        return result;
    }

    public static void main (String args[]) {
        int[] a = {121, 144, 19, 161, 19, 144, 19, 11};
        int[] b = {121,14641,20736,361,25921,361,20736,361};

        System.out.println(comp(a,b));
    }
}