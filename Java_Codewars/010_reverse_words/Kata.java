import java.util.*;

public class Kata
{
    public static String reverseWords(final String original)
    {
        if (original.isBlank()) {
            return original;
        }

        String[] array = original.split(" ");

        for (int i=0;i<array.length;i++) {
            StringBuffer temp = new StringBuffer(array[i]);
            array[i] = temp.reverse().toString();
        }  

        return String.join(" ",array);
    }

    public static void main(String args[]) {
        System.out.println(reverseWords("Wlazl kotek na plotek i mruga"));
    }
}