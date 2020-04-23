import java.util.ArrayList;
import java.util.Arrays;

class Metro {

    public static int countPassengers(ArrayList<int[]> stops) {
        int ppl = 0;

        for (int[] stop : stops) {
            //System.out.println(Arrays.toString(stop));
            ppl+=stop[0]-stop[1];
            //System.out.println(stop[0]+" ciastko "+stop[1]);

        }  
        //System.out.println("Number of people in the bus: "+ppl);
        return ppl;
    }

    public static void main (String args[]) {
        ArrayList<int[]> stops = new ArrayList<>();
        stops.add(new int[] {10,0});
        stops.add(new int[] {3,5});
        stops.add(new int[] {2,5});        
        
        Metro.countPassengers(stops);
    }
}