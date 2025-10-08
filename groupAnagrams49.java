import java.util.*;

public class groupAnagrams49 {
	
	public static void main(String[] args) {
		
		String [] strs = {"bdddddddddd","bbbbbbbbbbc"};
		System.out.println(groupAnagrams(strs));
	}
	
	
	private static List<List<String>> groupAnagrams(String[] strs) {
		 
		HashMap<String, List<String>> ans = new HashMap<>();
		 
		for (String s: strs) {
			
			int [] alphabets = new int[26];
			 
			for (char c: s.toCharArray()) {
				int index =  c - 'a';
				alphabets[index] += 1;
			}
			
			StringBuilder sb = new StringBuilder();
			for (int c: alphabets) {
				sb.append(c).append('#');
			}
			
			if (!ans.containsKey(sb.toString())) {
				ans.put(sb.toString(), new ArrayList<>());
			}
			ans.get(sb.toString()).add(s);
			
		 }
		 
		 return new ArrayList<>(ans.values());
		 
	 }
}
