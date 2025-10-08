import java.util.*;

public class longestConsecutiveSeq128 {
	
	public static void main (String [] args) {
		
		int [] nums = {100,4,200,1,3,2};
		
		System.out.println(longestConsecutive(nums));
		
	}
	
	private static int longestConsecutive(int[] nums) {
		
		Set<Integer> set = new HashSet<>();
		
		int maxAns = 0;
		
		for (int n: nums) {
			set.add(n);
		}
		
		for (Integer n: set) {
			int max = 0;
			
			if (!set.contains(n-1)) {
				while (set.contains(n + max)) {
					max += 1;
				}
			}
			
			maxAns = Math.max(max, maxAns);
		}
		
		return maxAns;		
	}
}
	
