import java.util.HashSet;
import java.util.Set;

public class CountingDuplicates {
	public static int duplicateCount(String text) {
		Set<Character> duplicates = new HashSet<>();
		Set<Character> signs = new HashSet<>();
		for (char c : text.toLowerCase().toCharArray()) {
			if (signs.contains(c)) {
				duplicates.add(c);
			} else {
				signs.add(c);
			}
		}
		return duplicates.size();
	}

	public static void main(String[] args) {
		System.out.println(duplicateCount("abcde"));
		System.out.println(duplicateCount("abcdea"));
		System.out.println(duplicateCount("indivisibility"));
	}
}

//0, CountingDuplicates.duplicateCount("abcde")
//1, CountingDuplicates.duplicateCount("abcdea"));
//1, CountingDuplicates.duplicateCount("indivisibility"));