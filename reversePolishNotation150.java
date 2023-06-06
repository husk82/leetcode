import java.util.*;

public class reversePolishNotation150 {
	
	public static void main (String [] args) {
		System.out.println(evalRPN(new String [] {"10","6","9","3","+","-11","*","/","*","17","+","5","+"}));
	}
	
	public static int evalRPN(String[] tokens) {
				
		Stack<Integer> stack = new Stack<>();
		int fir, sec, res;
		
		for (String token: tokens) {
			
			if (token.equals("+")) {
				sec = stack.pop();
				fir = stack.pop();
				res = fir + sec;
				System.out.println(fir + " + " + sec + " = " + res);
				stack.push(res);
			}
			else if (token.equals("-")) {
				sec = stack.pop();
				fir = stack.pop();
				res = fir - sec;
				System.out.println(fir + " - " + sec + " = " + res);
				stack.push(res);
			}
			else if (token.equals("/")) {
				sec = stack.pop();
				fir = stack.pop();
				res = fir / sec;
				System.out.println(fir + " / " + sec + " = " + res);
				stack.push(res);
			}
			else if (token.equals("*")) {
				sec = stack.pop();
				fir = stack.pop();
				res = fir * sec;
				System.out.println(fir + " * " + sec + " = " + res);
				stack.push(res);
			}
			else {
				stack.push(Integer.parseInt(token));
			}
		}
		return stack.peek();
	}
	
}
