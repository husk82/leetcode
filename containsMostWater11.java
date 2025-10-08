import java.util.*;

public class containsMostWater11 {
	
	public static void main (String [] args) {
		
		System.out.println("Max: " + maxArea(new int [] {1,8,6,2,5,4,8,3,7}));
		
	}
	
	private static int maxArea(int[] height) {
		
		int max = 0;
		
		int l = 0;
		int r = height.length - 1;
		
		while (l < r) {	
			if (height[l] > height[r]) {
				max = Math.max(max, height[r] * (r-l));
				r--;
			}
			else {
				max = Math.max(max, height[l] * (r-l));
				l++;
			}
		}
		return max;
	}
	
}
