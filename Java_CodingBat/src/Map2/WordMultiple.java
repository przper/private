package Map2;

import java.util.HashMap;
import java.util.Map;

public class WordMultiple {
	public Map<String, Boolean> wordMultiple(String[] strings) {
		Map<String, Boolean> map = new HashMap<>();
		for (String s : strings) {
			boolean flag = (map.containsKey(s) ? true : false);
			map.put(s, flag);
		}
		return map;
	}

}
