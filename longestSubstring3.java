import java.util.HashMap;

public class longestSubstring3 {

    public static void main (String []args) {
        System.out.println(lengthOfLongestSubstring("abcabcbb"));
    }

    private static int lengthOfLongestSubstring(String s) {
        int left = 0;
        int right = 1;
        int streak = 1;
        int maxStreak = 1;

        while (left < s.length() && right < s.length()) {
            System.out.println(s.charAt(left) + " - " + s.charAt(right));
            if (s.charAt(left) == s.charAt(right)) {
                streak = 0;
                left++;
                right = left + 1;
            }
            else {
                streak += 1;
                right++;
            }
            maxStreak = Math.max(maxStreak,streak);
        }

        return maxStreak;
    }

}
