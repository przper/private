package Functional1;

import java.util.List;

public class Square {
	public List<Integer> square(List<Integer> nums) {
		nums.replaceAll(i -> i * i);
		return nums;
	}

}
