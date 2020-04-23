package Functional2;

import java.util.List;

public class NoNeg {
	public List<Integer> noNeg(List<Integer> nums) {
		nums.removeIf(i -> i < 0);
		return nums;
	}
}
