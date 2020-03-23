import java.util.Arrays;

public class Clurgo {
	public static boolean anagramPairTest(String firstWord, String secondWord) {
		if(firstWord.length()!=secondWord.length()) {
			return false;
		}
		
		char[] firstList = firstWord.toCharArray();
		char[] secondList = secondWord.toCharArray();
		Arrays.sort(firstList);
		Arrays.sort(secondList);

		for(int i=0; i<firstList.length;i++) {
			if(firstList[i]!=secondList[i]) {
				return false;
			}
		}
		
		return true;
	}
	
	public static void main(String[] args) {
		System.out.println(anagramPairTest("narty","tyran"));
	}
}
