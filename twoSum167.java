import java.util.*;

public class twoSum167 {
	
	public int[] twoSum(int[] numbers, int target) {
		
		int l = 0;
		int r = numbers.length - 1;
		int sum = -1;
		
		while (sum != target) {
			sum = numbers[l] + numbers[r];
			if (sum > target) {
				r--;
			}
			else if (sum < target) {
				l++;
			}
		}
		
		return new int[] {l+1, r+1};
	}
}
