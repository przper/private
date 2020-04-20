package Map2;
import java.util.HashMap;
import java.util.Map;

public class WordCount {
	public Map<String, Integer> wordCount(String[] strings) {
		Map<String, Integer> map = new HashMap<>();
		for (String s : strings) {
			int n = (map.containsKey(s)) ? map.get(s) + 1 : 1;
			map.put(s, n);
		}
		return map;
	}

}
