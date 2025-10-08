import java.util.Arrays;

public class productOfArrayExceptSelf238 {
	
	public static void main (String[] args) {
		
		int[] nums = {1,2,3,4};
		System.out.println(Arrays.toString(productExceptSelf(nums)));
	}
	
	private static int[] productExceptSelf(int[] nums) {
	     
		int[] array = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            array[i] = 1;
        }
        
		int prefix = 1, postfix = 1;
		
		for (int i=0; i<nums.length; i++) {
			array[i] = prefix;
			prefix *= nums[i];
		}
		
		System.out.println(Arrays.toString(array));
		
		for (int i=nums.length-1; i>=0; i--) {
			array[i] *= postfix;
			postfix *= nums[i];
		}
		
		return array;
		 
	}
}
