public class TheOffice {

	public static String broken(final String x) {
		StringBuilder sb = new StringBuilder();
		for (char c : x.toCharArray()) {
			if (c == '0') {
				sb.append('1');
			} else if (c == '1') {
				sb.append('0');
			}
		}
		return sb.toString();
	}

	public static void main(String[] args) {
		System.out.println("normal: " + "0");
		System.out.println("broken: " + broken("0"));
		System.out.println("normal: " + "01111111010010000001100110111");
		System.out.println("broken: " + broken("01111111010010000001100110111"));
		System.out.println("normal: " + "011101");
		System.out.println("broken: " + broken("011101"));
	}
}