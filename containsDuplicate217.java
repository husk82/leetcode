import java.util.*;

public class containsDuplicate217 {
	
	public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> num = new HashSet<>();
        
        for (int i=0; i<nums.length; i++) {
        	if (num.contains(nums[i])){
        		return true;
        	}
        	else {
        		num.add(nums[i]);
        	}
        }
        
        return false;
    } 
}
