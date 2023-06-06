import java.util.*;

public class generateParentheses22 {
	
	public static void main (String [] args) {
		System.out.println(generateParenthesis(4));
	}
	
	public static List<String> generateParenthesis(int n) {
		List<String> list = new ArrayList<>();
		backtrack(n, 0, 0, new StringBuilder(), list);
		return list;
	}
	
	public static void backtrack(int n, int opened, int closed, StringBuilder build, List<String> list) {
		
		if ((opened == n) && (closed == n)) {
			list.add(build.toString());
			return;
		}
		if (opened < n) {
			build.append("(");
			backtrack(n, opened + 1, closed, build, list);
			build.deleteCharAt(build.length() - 1);
		}
		if (closed < opened) {
			build.append(")");
			backtrack(n, opened, closed + 1, build, list);
			build.deleteCharAt(build.length() -1);
		}
	}
	
}
