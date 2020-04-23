import java.util.LinkedList;
import java.util.List;

public class AreSame {

	public static boolean comp(int[] a, int[] b) {
		if (a==null || b==null) {
			return false;
		} else if (a.length==0 || b.length==0) {
			return true;
		}
		System.out.println("a: "+a.toString());
		System.out.println("a: "+b.toString());
		
		List<Integer> listA = new LinkedList<>();
		List<Integer> listB = new LinkedList<>();
		for (int num : a) {
			listA.add(num);
		}
		for (int num : b) {
			listB.add(num);
		}
		System.out.println("a: "+listA.toString());
		System.out.println("b: "+listB.toString());
		
		for (int num : listA) {
			System.out.println(num);
			if (!listB.contains(num*num)) {
				return false;
			} else {
				System.out.println("need to remove "+num*num);
				System.out.println("i= "+listB.indexOf(num*num));
				listB.remove(listB.indexOf(num*num));
				System.out.println(listB.toString());
			}
		}
		
		return true;
	}

	public static void main(String[] args) {
		int[] a = new int[] { 121, 144, 19, 161, 19, 144, 19, 11 };
		int[] b = new int[] { 121, 14641, 20736, 361, 25921, 361, 20736, 361 };
		System.out.println(comp(a, b));
	}

}