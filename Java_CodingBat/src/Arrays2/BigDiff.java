package Arrays2;

public class BigDiff {
	public int bigDiff(int[] nums) {
		int min = nums[0];
		int max = nums[0];
		for (int n : nums) {
			min = Math.min(n, min);
			max = Math.max(n, max);
		}
		return max-min;
	}
}
