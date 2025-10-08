import java.util.*;

public class slidingWindowMax239 {

	public static void main (String [] args) {
		System.out.println(Arrays.toString(maxSlidingWindow(new int[] {1,3,-1,-3,5,3,6,7}, 3)));
	}
	
	public static int[] maxSlidingWindow(int[] nums, int k) {
		
		int n = nums.length;
        int[] result = new int[n - k + 1];
        int index = 0;

        Deque<Integer> deque = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            // Remove elements that are out of the current window
            if (!deque.isEmpty() && deque.peekFirst() < i - k + 1) {
                deque.removeFirst();
            }

            // Remove elements smaller than the current element from the deque
            while (!deque.isEmpty() && nums[deque.peekLast()] < nums[i]) {
                deque.removeLast();
            }

            deque.addLast(i);

            // Start adding the maximum element to the result array after the first window
            if (i >= k - 1) {
                result[index++] = nums[deque.peekFirst()];
            }
        }

        return result;
    }
}
