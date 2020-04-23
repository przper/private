package Functional2;

import java.util.List;

public class NoZ {
	public List<String> noZ(List<String> strings) {
		strings.removeIf(s->s.contains("z"));
		return strings;
	}

}
