package przper_highest_scoring_word;

import java.util.Arrays;

public class Kata {

  public static String high(String s) {
      String[] words = s.split(" ");
      String result = words[0];
      for (int i=1; i<words.length; i++) {
          if (getPoints(result)<getPoints(words[i]) && getPoints(result) != getPoints(words[i])) {
              result = words[i];
          }
      }
      
      return result;
  }
  
  public static int getPoints (String word) {
      char[] alphabet = "abcdefghijklmnopqrstuvwxyz".toCharArray();
      int result = 0;
      
      for (char l : word.toCharArray()) {
          result+=Arrays.binarySearch(alphabet,l)+1;
      }
       
      return result;

  }
  
  public static void main(String args[]) {
      System.out.println(getPoints("volcano"));
      System.out.println(high("azzzzc what time are we climbing up to the volcano zzzzca"));
  }

}
