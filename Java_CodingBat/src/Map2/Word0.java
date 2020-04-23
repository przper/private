package Map2;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Word0 {
	public Map<String, Integer> word0(String[] strings) {
		Map<String, Integer> map = new HashMap<String, Integer>();
		for (String s : strings) {
			map.put(s, 0);
		}
		return map;
	}

}

//return Arrays.stream(strings).map(s -> new String[] { s, "0" }).collect(Collectors.toMap(p -> p[0], 0));
