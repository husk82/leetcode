import java.util.*;

public class threesum15 {
	
	public static void main (String [] args) {
		
		System.out.println(threeSum(new int [] {-2,0,0,2,2}));
		
	}
	
	private static List<List<Integer>> threeSum(int[] nums){
		
		Arrays.sort(nums);
		
		List<List<Integer>> list = new ArrayList<>();
		
		for (int i = 0; i < nums.length - 2; i++) {
			
			
			if ( i > 0 && nums[i] == nums[i-1]) {
				continue;
			}
			
			int l = i+1;
			int r = nums.length-1;
			
			while (l < r) {
				if (nums[i] + nums[l] + nums[r] == 0) {
					list.add(new ArrayList<>(List.of(nums[i], nums[l], nums[r])));
					l++;
					while (nums[l] == nums[l-1] && l < r) {
						l++;
					}
				}
				if (nums[i] + nums[l] + nums[r] > 0) {
					r--;
				}
				else if (nums[i] + nums[l] + nums[r] < 0) {
					l++;
				}
			}
		}
		return list;
		
	}
}
