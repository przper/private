
import java.util.Arrays;
import java.util.TreeMap;

public class Order {

    public static String order(String words) {
        TreeMap<Integer, String> map = new TreeMap<>();
        for (String word : words.split(" ")) {
            map.put(findNumber(word), word);
        }
        return String.join(" ", map.values());
    }

    public static int findNumber(String word) {
        char[] numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9'};
        int result = 0;
        for (char c : word.toCharArray()) {
            for (char num : numbers) {
                if (num == c) {
                    result = Character.getNumericValue(c);
                }
            }
        }

        return result;
    }

    public static void main(String args[]) {
        System.out.println(order("4of Fo1r pe6ople g3ood th5e the2"));
    }
}
