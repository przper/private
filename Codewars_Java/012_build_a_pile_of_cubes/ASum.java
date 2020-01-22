public class ASum {

    public static long findNb(long m) {
        long i = 0;
        long v = 0;

        while (v <= m) {

            if (v == m) {
                return i;
            }

            i++;
            v+=i*i*i;
        }
        return -1;
    }   

}