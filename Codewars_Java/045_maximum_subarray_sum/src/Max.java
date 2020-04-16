import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class Max {
	public static int sequence(int[] arr) {
		int[] arrSorted = arr.clone();
		Arrays.sort(arrSorted);
		
		if (arr.length==0) {
			return 0;
		} else if (arrSorted[arrSorted.length-1] <0) {
			return 0;
		}
		
		List<Integer> array = new LinkedList<>();
		for (int i : arr) {
			array.add(i);
		}
		
		List<Integer> result = new LinkedList<>();
		for (int i=0;i<arr.length;i++) {
			for (int j=i;j<array.size()+1;j++) {
				//System.out.println("i: "+i+", j: "+j);
				//System.out.println("sublist: "+array.subList(i, j));
				if (sum(result) < sum(array.subList(i, j))) {
					result = array.subList(i, j);
				}
			}
		}
		
		//array.forEach(System.out::println);
		return sum(result);
	}
	
	public static int sum(List<Integer> list) {
	     int sum = 0; 
	     for (int i : list)
	         sum += i;
	     return sum;
	}

	public static void main(String[] args) {
		System.out.println(sequence(new int[] { -2}));
		System.out.println(sequence(new int[] {}));
		System.out.println(sequence(new int[] { -2, 1, -3, 4, -1, 2, 1, -5, 4 }));
	}
}
//assertEquals("Empty arrays should have a max of 0", 0, Max.sequence(new int[]{}));
//assertEquals("Example array should have a max of 6", 6, Max.sequence(new int[]{-2, 1, -3, 4, -1, 2, 1, -5, 4}));