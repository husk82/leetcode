import java.util.*;

public class longestSubstring3 {

    public static void main (String []args) {
        System.out.println(lengthOfLongestSubstring("abcabcbb"));
    }

    private static int lengthOfLongestSubstring(String s) {
    	
    	if (s.length() == 0) return 0;
    	
        int left = 0;
        int right = 1;
        int maxStreak = 1;
        Set<Character> set = new HashSet<>();

        while (left < s.length() && right < s.length()) {
        	set.add(s.charAt(left));
            if (set.contains(s.charAt(right))) {
                set.clear();
                left++;
                right = left + 1;
            }
            else {
            	set.add(s.charAt(right));
                right++;
            }
            maxStreak = Math.max(maxStreak,set.size());
        }

        return maxStreak;
    }

}
