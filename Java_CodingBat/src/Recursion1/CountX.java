package Recursion1;

public class CountX {
	public int countX(String str) {
		if (str.length() <= 1) {
			if (str.contains("x")) {
				return 1;
			} else {
				return 0;
			}
		} else {
			if (str.charAt(0) == 'x') {
				return 1 + countX(str.substring(1));
			} else {
				return 0 + countX(str.substring(1));
			}
		}
	}

}
