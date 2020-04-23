
import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.Arrays;
import java.util.Collections;

public class NumberZooPatrol {

	public static int findMissingNumber1(int[] numbers) {
		Arrays.sort(numbers);
		//System.out.println(Arrays.toString(numbers));
		for (int i = 0; i < numbers.length; i++) {
			//System.out.println("Index: "+(i+1)+", number: "+numbers[i]);
			if (i+1 != numbers[i]) {
				return i+1;
			}
		}
		return 0;
	}
	
    public static int findMissingNumber(int[] numbers) {
    	long correctSum = (numbers.length+1) * (numbers.length+2) / 2;
    	long arraySum = Arrays.stream(numbers).reduce(0,  Integer::sum);
        return (int) (correctSum - arraySum);
    }
	
	public static void main(String[] args) {
		int[] array = new int[] {13, 11, 10, 3, 2, 1, 4, 5, 6, 9, 7, 8};
		System.out.println(findMissingNumber(array));
	}

}
