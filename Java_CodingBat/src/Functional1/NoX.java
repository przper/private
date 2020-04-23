package Functional1;

import java.util.List;

public class NoX {
	public List<String> noX(List<String> strings) {
		strings.replaceAll(s -> s.replace("x", ""));
		return strings;
	}

}
