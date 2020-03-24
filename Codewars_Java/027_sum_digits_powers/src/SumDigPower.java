import java.util.LinkedList;
import java.util.List;

public class SumDigPower {
	public static List<Long> sumDigPow(long a, long b) {
		List<Long> result = new LinkedList<>();
		for (long num = a; num < b; num++) {
			char[] numInChar = String.valueOf(num).toCharArray();
			long sum = 0;
			for (int i = 0; i < numInChar.length; i++) {
				sum += Math.pow(Character.getNumericValue(numInChar[i]), i + 1);
			}
			if (num == sum) {
				result.add(num);
			}
		}
		return result;
	}
}
