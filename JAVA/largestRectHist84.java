import java.util.*;

public class largestRectHist84 {

	public int largestRectangleArea(int[] heights) {
		
		if (heights.length == 0) return heights.length;
		
		int maxArea = 0;
		
		Stack<Integer> index = new Stack<>();
		
		for (int i=0; i<heights.length; i++) {
			int h = (i == heights.length) ? 0 : heights[i];
	        while (!index.isEmpty() && h < heights[index.peek()]) {
	            int pop = index.pop();
	            int height = heights[pop];
	            int width = index.isEmpty() ? i : i - index.peek() - 1;
	            maxArea = Math.max(height * width, maxArea);
	        }
	        index.push(i);	
		}
		
		while (!index.isEmpty()) {
			int pop = index.pop();
			int height = heights[pop];
			int width = index.empty() ? heights.length : heights.length - index.peek() - 1;
			maxArea = Math.max(height * width, maxArea);
		}
		
		return maxArea;
	}
		
}
	

