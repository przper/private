package Map2;

import java.util.HashMap;
import java.util.Map;

public class FirstSwap {
	public String[] firstSwap(String[] strings) {
		String[] result = strings.clone();
		Map<String, Integer> map = new HashMap<>();
		for (int i = 0; i < strings.length; i++) {
			String firstChar = Character.toString(strings[i].charAt(0));
			if (map.containsKey(firstChar) && map.get(firstChar) != -1) {
				int tmp = map.get(firstChar);
				result[map.get(firstChar)] = strings[i];
				result[i] = strings[tmp];
				map.put(firstChar, -1);
			} else if (map.containsKey(firstChar) && map.get(firstChar) == -1) {
				map.put(firstChar, -1);
			} else {
				map.put(firstChar, i);
			}
		}
		return result;
	}

}
