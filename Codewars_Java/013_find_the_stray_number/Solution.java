class Solution {
    static int stray(int[] numbers) {
        int[] first = {numbers[0],0};
        int[] second = {0,0};
        for (int i = 1; i<numbers.length;i++) {
            if (numbers[i] != numbers[0]) {
                second[0]=numbers[i];
                second[1] += 1;
            } else {
                first[1] += 1;
            }
        }

        if (first[1]<second[1]) {
            return first[0];
        } else {
            return second[0];
        }   
    }

    public static void main (String args[]) {
        int[] array = {17, 17, 3, 17, 17, 17, 17};
        System.out.println(stray(array));
    }
}