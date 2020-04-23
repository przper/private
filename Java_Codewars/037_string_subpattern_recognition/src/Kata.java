public class Kata {

	public static boolean hasSubpattern(String str) {
		StringBuilder pattern = new StringBuilder();
		int i = 0;
		while (pattern.length() < str.length() / 2) {
			pattern.append(str.charAt(i));
			StringBuilder substring = new StringBuilder(pattern);
			System.out.println("Pattern: " + pattern.toString());
			System.out.println(str.length() + " / " + pattern.length() + " = " + (str.length() / pattern.length()));
			for (int j = 0; j < (str.length() / pattern.length()-1); j++) {
				substring.append(pattern);
			}
			System.out.println("String: "+substring.toString());
			System.out.println("Input:  "+str.toString());
			
			if (substring.toString().equals(str)) {
				return true;
			}

			i++;
		}

		return false;
	}

	public static void main(String[] args) {
		System.out.println(hasSubpattern("abcdef") + "\n");
		System.out.println(hasSubpattern("aaaa") + "\n");
		System.out.println(hasSubpattern("abababab") + "\n");
	}
}
/*
 * assertFalse(Kata.hasSubpattern("a"));
 * assertTrue(Kata.hasSubpattern("aaaa"));
 * assertFalse(Kata.hasSubpattern("abcd"));
 * assertTrue(Kata.hasSubpattern("abababab"));
 * assertFalse(Kata.hasSubpattern("ababababa"));
 * assertTrue(Kata.hasSubpattern("123a123a123a"));
 * assertFalse(Kata.hasSubpattern("123A123a123a"));
 * assertTrue(Kata.hasSubpattern("abbaabbaabba"));
 * assertFalse(Kata.hasSubpattern("abbabbabba"));
 * assertFalse(Kata.hasSubpattern("abcdabcabcd"));
 */