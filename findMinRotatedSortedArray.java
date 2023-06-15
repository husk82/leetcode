import java.util.*;

public class findMinRotatedSortedArray {
	
	public static void main (String [] args) {
		
		System.out.println(findMin(new int[] {4,5,6,7,0,1,2}));
		
	}
	
	public static int findMin(int[] nums) {
		
		int l = 0;
		int r = nums.length - 1;
		
		while (l < r) {
			
			int midpoint = (l + r) / 2;

			if (nums[midpoint] < nums[r]) {
				r = midpoint;
			}
			else {
				l = midpoint + 1;
			}
		}
		return nums[l];
	}
	
}
