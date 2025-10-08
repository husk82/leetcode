import java.util.*;

public class longestRepeatingCharacter424 {
	
	public static void main (String [] args) {
		System.out.println(characterReplacement("AABABBA", 1	));
	}
	
	private static int characterReplacement(String s, int k) {
        
		int left = 0;
		int max = 0;
		
		HashMap<Character, Integer> map = new HashMap<>();
		
		for (int right=0; right<s.length(); right++) {
			map.put(s.charAt(right), 1 + getValue(map, s.charAt(right)));
			
			if (((right-left+1 - getMaxValue(map))) > k) {
				map.put(s.charAt(left), getValue(map, s.charAt(left)) - 1);
				left++;
			}
			
			max = Math.max(max, right - left + 1);
		}
		
		return max;
		
    }
	

    private static int getMaxValue(HashMap<Character, Integer> hashMap) {
        int maxValue = Integer.MIN_VALUE;

        for (Map.Entry<Character, Integer> entry : hashMap.entrySet()) {
            int value = entry.getValue();
            if (value > maxValue) {
                maxValue = value;
            }
        }

        return maxValue;
    }
	
    private static int getValue(HashMap<Character, Integer> hashMap, char c) {
    	if (!hashMap.containsKey(c)) return 0;
    	return hashMap.get(c);
    }
	
}	
