import java.util.*;

public class minStack155 {
	
	private Stack<Integer> stack;
    private Stack<Integer> minValue;
	
	public minStack155() {
		stack = new Stack<>();
		minValue = new Stack<>();
    }
    
    public void push(int val) {
    	stack.push(val);
    	if (minValue.isEmpty() || val < minValue.peek()) {
    		minValue.push(val);
    	}
    	else {
    		minValue.push(minValue.peek());
    	}
    }
    
    public void pop() {
        stack.pop();
        minValue.pop();    
    }
    
    public int top() {
        return stack.peek();    
    }
    
    public int getMin() {
        return minValue.peek();
    }
}
