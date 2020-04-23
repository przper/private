
public class Ball {

    public static int maxBall(int v0) {
        int i = 0;
        double time = 0;
        double v = (double) v0 * 1000 / 3600;
        double height = 0;
        double maxHeight = 0;

        while (maxHeight <= height) {
            System.out.println("Im in loop number: " + i);
            System.out.println("Time: " + time);
            System.out.println("Height: " + height);
            maxHeight = height;
            
            i++;
            time = (double) i / 10;
            height = (double) v * time - 0.5 * 9.81 * time * time;
        }
        
        System.out.println("Max height: " + maxHeight);
        return i-1;
    }

    public static void main(String args[]) {
        System.out.println(maxBall(15));
    }
}
