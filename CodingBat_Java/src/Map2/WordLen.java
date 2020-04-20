package Map2;

import java.util.HashMap;
import java.util.Map;

public class WordLen {
	public Map<String, Integer> wordLen(String[] strings) {
		  Map<String,Integer> map = new HashMap<String,Integer>();
		  for (String s : strings) {
			  map.put(s, s.length());
		  }
		  return map;
	}

}
