package Arrays2;

import java.util.Arrays;

import javax.xml.transform.stream.StreamSource;

public class CountEvens {
	public int countEvens(int[] nums) {
		  return (int) Arrays
				  .stream(nums)
				  .filter(s->s%2==0)
				  .count();
	}
}
