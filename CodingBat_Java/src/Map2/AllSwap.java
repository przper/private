package Map2;

import java.util.HashMap;
import java.util.Map;

public class AllSwap {
	public String[] allSwap(String[] strings) {
		String[] result = strings.clone();
		Map<String, Integer> map = new HashMap<>();
		for (int i = 0; i < strings.length; i++) {
			String firstChar = Character.toString(strings[i].charAt(0));
			if (map.containsKey(firstChar)) {
				int tmp = map.get(firstChar);
				result[map.get(firstChar)] = strings[i];
				result[i] = strings[tmp];
				map.remove(firstChar);
			} else {
				map.put(firstChar, i);
			}
		}
		return result;
	}

}
