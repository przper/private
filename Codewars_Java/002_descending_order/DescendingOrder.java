import java.util.Arrays;

public class DescendingOrder {
  public static int sortDesc(final int num) {
    //#1 take the num and slice it into Array of chars
    char[] chars = Integer.toString(num).toCharArray();
    
    //#2 use array built-in method to sort the chars
    Arrays.sort(chars);
    //could be done with Str[], .split()
    
    
    //#3 reverse it
    String sorted = String.valueOf(chars);
    String reverse = "";
    
    for (int i = sorted.length()-1; i>=0 ; i--){
        reverse += sorted.charAt(i);
    }
    //could be done with Arrays.sort(x,Collections.reverseOrder()) in 1 line
    
    
   //#4 convert string to integer
   return Integer.parseInt(reverse);
  }
}