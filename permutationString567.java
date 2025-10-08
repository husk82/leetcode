import java.util.*;


public class permutationString567 {
	
	public static void main (String [] args) {
		System.out.println(checkInclusion("ab", "eidbaooo"));	}
	
	private static boolean checkInclusion(String s1, String s2) {
		
		if (s1.length() > s2.length()) return false;
		
		int[] s1Map = new int[26];
		int[] s2Map = new int[26];
		
		for (int i = 0; i < s1.length(); i++) {
			s1Map[(int) s1.charAt(i) - (int) 'a'] += 1;
			s2Map[(int) s2.charAt(i) - (int) 'a'] += 1;
		}
		
		int matches = 0;
		
		for (int i=0; i<26; i++) {
			if (s1Map[i] == s2Map[i]) {
				matches += 1;
			}
		}
		
		int l = 0;
		
		for (int r = s1.length(); r<s2.length(); r++) {
			
			if (matches == 26) return true;
			
			int index = (int) s2.charAt(r) - (int) 'a';
			s2Map[index] += 1;
			if (s1Map[index] == s2Map[index]) {
				matches += 1;
			}
			else if (s1Map[index] + 1 == s2Map[index]) {
				matches -= 1;
			}
			
			index = (int) s2.charAt(l) - (int) 'a';
			s2Map[index] -= 1;
			if (s1Map[index] == s2Map[index]) {
				matches += 1;
			}
			else if (s1Map[index] - 1 == s2Map[index]) {
				matches -= 1;
			}
			
			l += 1;
		}
		
		return (matches == 26);
	}
}