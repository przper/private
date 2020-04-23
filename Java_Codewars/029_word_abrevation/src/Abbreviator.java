public class Abbreviator {

	public static String abbreviate(String string) {
		StringBuilder result = new StringBuilder();
		String[] pieces = string.split("(?<=[a-zA-Z])(?=[^a-zA-Z])|(?<=[^a-zA-Z])(?=[a-zA-Z])");
		//String[] pieces = string.split("(?<=\\w)(?=\\W)|(?<=\\W)(?=\\w)");
		for (String s : pieces) {
			if (s.length() >= 4) {
				StringBuilder sb = new StringBuilder();
				sb.append(s.charAt(0));
				sb.append(String.valueOf(s.length() - 2));
				sb.append(s.charAt(s.length() - 1));
				s = sb.toString();
				result.append(s);
			} else {
				result.append(s);
			}
		}
		return result.toString();
	}

	public static void main(String[] args) {
		System.out.println(abbreviate("internationalization"));
		System.out.println(abbreviate("elephant-rides are really fun!"));
		System.out.println(abbreviate("balloon5double-barreled"));

	}

	// assertEquals("i18n", abbr.abbreviate("internationalization"));
}