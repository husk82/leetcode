import java.util.*;

public class dailyTemp739 {
	
	public static void main (String [] args) {
		
		System.out.println(Arrays.toString(dailyTemperatures(new int [] {73,74,75,71,69,72,76,73})));
		
	}
	
	public static int[] dailyTemperatures(int[] temperatures) {
		
		int[] result = new int [temperatures.length];		
		Stack<Integer> stack = new Stack<>();
		
		for (int i=0; i<temperatures.length; i++) {
			
			while (!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]) {
				int prev = stack.pop(); 
				result[prev] = i - prev;
			}
			stack.push(i);
	
		}
		return result;
	}
	
}
