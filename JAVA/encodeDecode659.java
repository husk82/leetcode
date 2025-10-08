import java.util.*;

public class encodeDecode659 {
	
	public static void main (String [] args) {
		
		List<String> list = new ArrayList<>();
		list.add("lint");
		list.add("code");
		list.add("love");
		
		String s = encode(list);
		System.out.println(s);
		
		System.out.println(decode(s));
		
	}
	
	private static String encode(List<String> strs) {
		 
		StringBuilder sb = new StringBuilder();
		 
		for (String s: strs) {
			sb.append(s.length() + "#" + s);
		}
		 
		return sb.toString();
	 }
	 
	 
	private static List<String> decode(String str) {
		 
		List<String> list = new ArrayList<>();
		
		int i = 0;
		
		while ( i < str.length()) {
			
			int j = i;
			
			while ( str.charAt(j) != '#') {
				j += 1;
			}
			
			list.add(str.substring((j + 1), j + 1 + Character.getNumericValue(str.charAt(j-1))));
			i = j + 1 + Character.getNumericValue(str.charAt(j-1));
		}
		
		return list;
		 
	}
	
}
