import java.util.*;

public class kokoEatingBananas875 {
	
	public static void main (String [] args) {
		
		System.out.println(minEatingSpeed(new int[] {3,6,7,11}, 8));
		
	}
	
	public static int minEatingSpeed(int[] piles, int h) {
		
		int l = 1;
		int r = Arrays.stream(piles).max().orElse(0);
		int res = r;
		
		while (l <= r) {
			int timeTaken = 0;
			int midpoint = (l + r) / 2;
			
			for (int p: piles) {
				timeTaken += Math.ceil((double) p/midpoint);
			};
			
			if (timeTaken > h) {
				l = midpoint + 1;
			}
			else {
				res = Math.min(midpoint, res);
				r = midpoint - 1;
			}
		}
		return res;
	}
	
}
