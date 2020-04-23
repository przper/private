import java.util.ArrayList;
import java.util.List;

class Solution {

	public static String binaryToText(String binary) {
		List<StringBuilder> sbArray = new ArrayList<>();
		StringBuilder result = new StringBuilder();
		StringBuilder sb = new StringBuilder();
		for (char c : binary.toCharArray()) {
			// System.out.println("char: "+c);
			sb.append(c);
			// System.out.println("StringBuilder: "+sb.toString());
			if (sb.length() == 8) {
				sbArray.add(sb);
				sb = new StringBuilder();
			}
		}

		for (StringBuilder s : sbArray) {
			//System.out.println(s.toString());
			int num = Integer.parseInt(s.toString(),2);
			char c = (char) num;
			//System.out.println(c);
			result.append(c);
		}

		return result.toString();
	}

	public static void main(String[] args) {
		// System.out.println(binaryToText("00000000"));
		// System.out.println(binaryToText("0100100001100101011011000110110001101111"));
		System.out.println(binaryToText("0100100001100101011011000110110001101111"));
		// System.out.println("hello".getBytes());

	}

}