import java.util.*;

public class SmileFaces {

    public static int countSmileys(List<String> arr) {
        int count = 0;
        String[] tmpl = {":-)",":-D",":~)",":~D",":)",":D",
                ";-)",";-D",";~)",";~D",";)",";D"};
        for (String word : arr) {
            for (String face : tmpl){
                if (word.equals(face)) {         
                    count+=1;
                }

            }

        }            

        return count;
    }
}