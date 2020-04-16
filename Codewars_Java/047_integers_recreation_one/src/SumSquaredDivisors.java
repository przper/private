import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

public class SumSquaredDivisors {

	public static String listSquared(long m, long n) {
		List<String> result = new ArrayList();
		for (int i : getNumbersInRange((int) m, (int) n)) {
			List<Integer> squared = new LinkedList<>();
			for (int j : getDivisors(i)) {
				squared.add(j*j);
			}
			if (checkPerfectSquare(getSum(squared))) {
				result.add(Arrays.toString(new int[] {i, getSum(squared)}));
			}
		}

		return result.toString();
	}

	public static List<Integer> getNumbersInRange(int start, int stop) {
		List<Integer> result = new LinkedList<>();
		for (int i = start; i <= stop; i++) {
			result.add(i);
		}
		return result;
	}

	public static int getSum(List<Integer> array) 
    { 
        int sum = 0;
        for (int i = 0; i < array.size(); i++) 
           sum +=  array.get(i); 
        return sum; 
    } 
	
	public static List<Integer> getDivisors(int number) {
		List<Integer> result = new LinkedList<>();
		for (int i = 1; i <= number; i++) {
			if (number % i == 0) {
				result.add(i);
			}
		}
		return result;
	}

	static boolean checkPerfectSquare(double x) {
		double sq = Math.sqrt(x);
		return ((sq - Math.floor(sq)) == 0);
	}
	
	

	public static void main(String[] args) {
		System.out.println(listSquared(1, 250));
		// System.out.println(listSquared(42, 250));
		// System.out.println(listSquared(250, 500));
	}
}

//[[1, 1], [42, 2500], [246, 84100]]", SumSquaredDivisors.listSquared(1, 250));
//[[42, 2500], [246, 84100]]", SumSquaredDivisors.listSquared(42, 250));
//[[287, 84100]]", SumSquaredDivisors.listSquared(250, 500));
