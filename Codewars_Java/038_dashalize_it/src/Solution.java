

public class Solution {

	public static String dashatize(int num) {
		String result = Integer.toString(num)
				.replaceAll("([13579])","-$1-")
				.replaceAll("--", "-")
				.replaceAll("^-","")
				.replaceAll("-$","");

		return result;
		
	}

	public static void main(String[] args) {
		System.out.println(dashatize(274));
		System.out.println(dashatize(5311));
		System.out.println(dashatize(86320));
		System.out.println(dashatize(974302));
	}

}

//assertEquals("2-7-4", Solution.dashatize(274));
//assertEquals("5-3-1-1", Solution.dashatize(5311));
//assertEquals("86-3-20", Solution.dashatize(86320));
//assertEquals("9-7-4-3-02", Solution.dashatize(974302));