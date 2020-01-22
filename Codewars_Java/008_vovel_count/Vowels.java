import java.util.Arrays;

public class Vowels {

    public static int getCount(String str) {
        int vowelsCount = 0;
        for (char letter : str.toCharArray()){
            if ("aeiou".contains(String.valueOf(letter))) {
                vowelsCount +=1;
            }
        }
        return vowelsCount;
    }

}