import java.util.HashMap;
import java.util.Map;

public class DuplicateEncoder {
	static String encode(String word) {
		Map<Character, Integer> map = new HashMap<Character, Integer>();
		for (char c : word.toLowerCase().toCharArray()) {
			if (map.containsKey(c)) {
				map.put(c, map.get(c) + 1);
			} else {
				map.put(c, 1);
			}
		}
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < word.length(); i++) {
			Character c = Character.toLowerCase(word.charAt(i));
			sb.append(map.get(c)>1 ? ")" : "(");
		}
		// System.out.println(map.toString());

		return sb.toString();
	}

	public static void main(String[] args) {
		System.out.println(encode("Prespecialized").equals(")()())()(()()("));
		// System.out.println(encode(" ()( "));
	}

}
// DuplicateEncoder.encode("Prespecialized")) ->")()())()(()()("
// DuplicateEncoder.encode(" ()( ")); "))))())))"
