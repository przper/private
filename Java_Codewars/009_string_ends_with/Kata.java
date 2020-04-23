public class Kata {
    public static boolean solution(String str, String ending) {

        StringBuffer strRev = new StringBuffer(str);
        StringBuffer endingRev = new StringBuffer(ending);

        strRev.reverse().toString();
        endingRev.reverse().toString();

        if (str.length() >= ending.length()) {

            for (int i = 0; i<ending.length();i++){
                if (strRev.charAt(i) != endingRev.charAt(i)) {
                    return false;
                }
            }

            return true;
        }
        else {
            return false;}
    }
}
