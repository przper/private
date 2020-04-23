package Functional1;

import java.util.List;

public class Lower {
	public List<String> lower(List<String> strings) {
		strings.replaceAll(s->s.toLowerCase());
		return strings;
	}

}
