import java.util.Arrays;

public class Solution
{
    public static int[] twoSum(int[] numbers, int target)
    {
        int[] result = {0, 0};

        for (int i = 0; i<numbers.length; i++) {
            for (int j = 0; j<numbers.length; j++) {
                if (numbers[i]+numbers[j]==target && i!=j) {
                    result[0]=i;
                    result[1]=j;
                }
            }
        }
        
        return result;
    }
}