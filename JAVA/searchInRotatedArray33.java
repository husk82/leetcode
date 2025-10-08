import java.util.*;

public class searchInRotatedArray33 {
	
	public static void main (String [] args) {
		
		System.out.println(search(new int [] {6,7,0,1,2,4,5}, 2));
		
	}
	
	public static int search(int[] nums, int target) {
		
		int l = 0;
		int r = nums.length - 1;
		
		while (l <= r) {
			
			int mid = (l+r) / 2;
			
			if (nums[mid] == target) {
				return mid;
			}
			// left 
			if (nums[mid] >= nums[l]) {
				if (target >= nums[l] && target < nums[mid]) {
					r = mid - 1;
				}
				else {
					l = mid + 1;
				}
			}
			// right
			else {
				if (target > nums[mid] && target <= nums[r]) {
					l = mid + 1;
				}
				else {
					r = mid - 1;
				}
			}
		}
		
		return -1;
	}
	
}
