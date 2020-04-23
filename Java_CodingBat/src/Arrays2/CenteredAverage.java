package Arrays2;

import java.util.Arrays;

public class CenteredAverage {
	public static int centeredAverage(int[] nums) {
		Arrays.sort(nums);
		int sum = 0;
		for (int i=1; i<=nums.length-2;i++) {
			sum+=nums[i];
		}
		return sum/(nums.length-2);
	}

	public static void main(String[] args) {
		int[] array = new int[] {1, 2, 3, 4, 100};
		System.out.println(centeredAverage(array));
	}
}
