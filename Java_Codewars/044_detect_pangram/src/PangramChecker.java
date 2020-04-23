public class PangramChecker {
	public boolean check(String sentence) {
		System.out.println(sentence);
		char[] chars = "abcdefghijklmnopqrstuvwxyz".toCharArray();
		for (Character c : chars) {
			if (!sentence.toLowerCase().contains(c.toString())) {
				return false;
			}
		}
		return true;
	}

	public static void main(String[] args) {

	}
}