
import java.util.Arrays;

public class Tortoise {

    public static int[] race(int v1, int v2, int g) {

        if (v1 > v2) {
            return null;
        }
        double time = (double) g / (v2 - v1);
        System.out.println(time);

        int hour = (int) time;
        int min = (int) (time * 60) % 60;
        int sec = (int) (time * (60 * 60)) % 60;

        int[] result = {hour, min, sec};
        return result;
    }

    public static void main(String args[]) {
        System.out.println(Arrays.toString(race(80, 100, 40)));
        System.out.println(Arrays.toString(race(720, 850, 70)));
        System.out.println(Arrays.toString(race(85, 72, 70)));
    }
}
