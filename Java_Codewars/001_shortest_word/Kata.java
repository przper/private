import java.util.Arrays;

public class Kata {
    public static int findShort(String s) {
        String[] array = s.split(" ",0);
        int l = s.length();
        for (String word : array){
            if (word.length()<l){
                l = word.length();
            }
        }
        return l;    
    }
}