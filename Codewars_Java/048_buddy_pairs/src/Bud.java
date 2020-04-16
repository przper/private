import java.util.LinkedList;
import java.util.List;
import java.util.stream.LongStream;

public class Bud {
	public static String buddy(long start, long limit) {
		for (long n = start; n<limit; n++) {
			if (n < sumOfDivisors(n)-1) {
				// System.out.println("Index: "+n+", Sum: "+ sumOfDivisors(n));
				long m = sumOfDivisors(n) - 1;
				// System.out.println("m: "+m+" sum: "+sumOfDivisors(m));
				if (sumOfDivisors(m) - 1 == n && m > n) {
					return (String.format("(%s %s)", n, m));
				}
			}

		}
		return "Nothing";
	}

	public static long sumOfDivisors(long number) {
		return LongStream.range(1, number).filter(i -> number % i == 0).sum();
	}

	public static void main(String[] args) {
		// System.out.println(buddy(381, 4318));
		// System.out.println(buddy(10, 50));
		System.out.println(buddy(1071625, 1103735));
	}
}

//testing(1071625, 1103735, "(1081184 1331967)");
//testing(2382, 3679, "Nothing");
//testing(381, 4318, "(1050 1925)");