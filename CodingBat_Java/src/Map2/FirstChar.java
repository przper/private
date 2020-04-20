package Map2;

import java.util.HashMap;
import java.util.Map;

public class FirstChar {
	public Map<String, String> firstChar(String[] strings) {
		Map<String, String> map = new HashMap<>();
		for (String s : strings) {
			String l = Character.toString(s.charAt(0));
			map.put(l, (map.containsKey(l) ? map.get(l).concat(s) : s));
		}
		return map;
	}

}
