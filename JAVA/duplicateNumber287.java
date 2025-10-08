import java.util.*;

public class duplicateNumber287 {
	
	public static void main (String [] args) {
		System.out.println(findDuplicate(new int [] {3,1,3,4,2}));
	}
	
	public static int findDuplicate(int[] nums) {
		int slow = 0;
        int fast = 0;

        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        }
        while (slow != fast);

        int slow2 = 0;
        do {
            slow2 = nums[slow2];
            slow = nums[slow];
        }
        while (slow2 != slow);
        return slow;
	}
}
