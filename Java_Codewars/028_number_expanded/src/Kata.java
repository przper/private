import java.util.LinkedList;
import java.util.List;

public class Kata {

	public static String expandedForm(int num) {
		List<String> array = new LinkedList<>();
		int numLength = String.valueOf(num).length();

		for (int i = 0; i < numLength; i++) {
			int c = Character.getNumericValue(String.valueOf(num).charAt(i));
			int power = (int) Math.pow(10, numLength - i - 1);
			if (c != 0) {
				array.add(String.valueOf(c * power));
			}
		}

		return String.join(" + ", array);

	}

	public static void main(String[] args) {
		System.out.println(expandedForm(12));
		System.out.println(expandedForm(42));
		System.out.println(expandedForm(70304));
		System.out.println(expandedForm(9000000));
	}
}