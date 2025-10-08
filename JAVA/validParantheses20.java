import java.util.*;

public class validParantheses20 {
	
	public boolean isValid(String s) {
		
		HashMap<Character, Character> map = new HashMap<>();
		map.put('}', '{');
		map.put(')', '(');
		map.put(']', '[');
		
		Stack<Character> stack = new Stack<>();
		
		if (s.charAt(0) == '}' || s.charAt(0) ==']' || s.charAt(0) == ')') return false;
		
		for (int i = 0; i < s.length(); i++) {
			
			if (map.containsKey(s.charAt(i))) {
				if (!stack.isEmpty() && stack.peek() == map.get(s.charAt(i))) {
					stack.pop();
				}
				else {
					return false;
				}
			}
			else {
				stack.add(s.charAt(i));
			}
			
		}
		return stack.isEmpty();
	}
	
}
