import java.util.*;

public class validPalindrome125 {
	
	public boolean isPalindrome(String s) {
		 int l = 0;
		 int r = s.length() - 1;
		 
		 s = s.toLowerCase();
		 
		 while (l < r) {
			 while (!Character.isLetterOrDigit(s.charAt(l)) && l < r) {
				 l++;
			 }
			 while (!Character.isLetterOrDigit(s.charAt(r)) && r > l) {
				 r--;
			 }
			 if (!(s.charAt(l) == s.charAt(r))) {
				 return false;
			 }
			 l++;
			 r--;
		 }
		 return true;
	}
}
