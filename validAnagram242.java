import java.util.*;

public class validAnagram242 {
	public boolean isAnagram(String s, String t) {
		char[] charS = s.toCharArray();
		Arrays.sort(charS);
		
		char[] charT = t.toCharArray();
		Arrays.sort(charT);
		
		return Arrays.equals(charT, charS);
    }
}
