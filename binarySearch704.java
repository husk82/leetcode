
public class binarySearch704 {
	
	public static void main (String [] args) {
		
		System.out.println(search(new int[] {-1,0,3,5,9,12}, 9));
	
	}
	
	public static int search(int[] nums, int target) {
		
		int l = 0;
		int r = nums.length - 1;
		
		while (l <= r) {
			
			int midpoint = (l + r) / 2; 
			
			if (nums[midpoint] == target) {
				return midpoint;
			}
			
			if (nums[midpoint] < target) {
				l = midpoint + 1;
			}
			
			if (nums[midpoint] > target) {
				r = midpoint - 1;
			}
		}
		return -1;	
	}
	
}
