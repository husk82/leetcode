import java.util.*;

public class reversePolishNotation150 {
	
	public static void main (String [] args) {
		System.out.println(evalRPN(new String [] {"10","6","9","3","+","-11","*","/","*","17","+","5","+"}));
	}
	
	public static int evalRPN(String[] tokens) {
				
		Stack<Integer> stack = new Stack<>();
		
		for (String token: tokens) {
			
			if (token.equals("+")) {
				int sec = stack.pop();
				int fir = stack.pop();
				stack.push(fir + sec);
			}
			else if (token.equals("-")) {
				int sec = stack.pop();
				int fir = stack.pop();
				stack.push(fir - sec);
			}
			else if (token.equals("/")) {
				int sec = stack.pop();
				int fir = stack.pop();
				stack.push(fir / sec);
			}
			else if (token.equals("*")) {
				int sec = stack.pop();
				int fir = stack.pop();
				stack.push(fir * sec);
			}
			else {
				stack.push(Integer.parseInt(token));
			}
		}
		return stack.peek();
	}
	
}
