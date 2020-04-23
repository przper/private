package Map2;

import java.util.HashMap;
import java.util.Map;

public class WordAppend {
	public static String wordAppend(String[] strings) {
		Map<String, Integer> map = new HashMap<>();
		StringBuilder sb = new StringBuilder();
		for (String s : strings) {
			int num = map.containsKey(s) ? map.get(s) + 1 : 1;
			map.put(s, num);
			if (map.get(s)%2==0) {
				sb.append(s);
			}
		}
		return sb.toString();
	}

	public static void main(String[] args) {
		System.out.println(wordAppend(new String[] {"a", "b", "b", "b", "a", "c", "a", "a", "a", "b", "a"}));
	}

}
