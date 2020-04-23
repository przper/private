import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

public class RevRot {

	public static String revRot(String strng, int sz) {
		// idiotproof
		if (sz <= 0 || sz > strng.length() || strng.isEmpty()) {
			return "";
		}
		System.out.println("input str: "+strng);
		System.out.println("input sz:  "+sz);
		List<String> chunks = new LinkedList<>();
		List<String> result = new LinkedList<>();
		

		// divide into chunks
		for (int i = 0; i < strng.length(); i += sz) {
			String chunk = strng.substring(i, Math.min(strng.length(), i + sz));
			if (chunk.length() == sz) {
				chunks.add(chunk);
			}
		}

		for (String chunk : chunks) {
			//System.out.println(chunk);
			int sum = 0;
			
			// create digits list
			List<Integer> digits = new LinkedList<>();
			for (Character c : chunk.toCharArray()) {
				digits.add(Character.getNumericValue(c));
			}
			//System.out.println(digits);

			// sum the digits' cubes
			for (int digit : digits) {
				sum += (int) Math.pow(digit, 3);
			}
			//System.out.println(sum);
			// check the condition
			if (sum % 2 == 0) {
				//System.out.println("reverse");
				Collections.reverse(digits);
				result.add(digits.toString());
				//System.out.println(digits.toString());

			} else {
				//System.out.println("rotate");
				Collections.rotate(digits, -1);
				result.add(digits.toString());
				//System.out.println(digits.toString());
			}
			//System.out.println("----------");
		}
		System.out.println("output: "+result.toString().replaceAll("[\\[\\],\\s]", ""));
		return result.toString().replaceAll("[\\[\\],\\s]", "");
	}

	public static void main(String[] args) {
		//System.out.println(revRot("123456987654", 6)); // 234561876549
		//System.out.println(revRot("12345678", 4));
		System.out.println(revRot("733049910872815764", 5));
		
	}
}

//System.out.println("Fixed Tests: revRot");   
//testing(RevRot.revRot("1234", 0), "");
//testing(RevRot.revRot("", 0), "");
//testing(RevRot.revRot("1234", 5), "");
//String s = "733049910872815764";
//testing(RevRot.revRot(s, 5), "330479108928157");