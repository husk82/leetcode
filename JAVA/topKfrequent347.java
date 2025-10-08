import java.util.*;
import java.util.Map.Entry;

public class topKfrequent347 {
	
	public static void main (String [] args) {
		
		int [] nums = {4,1,-1,2,-1,2,3};
		
		System.out.println(Arrays.toString(topKFrequent(nums , 2)));
		
	}
	
	private static int[] topKFrequent(int[] nums, int k) {
        
		HashMap<Integer, Integer> ans = new HashMap<>();
		
		for (int i=0; i<nums.length; i++) {
			ans.put(nums[i], ans.getOrDefault(nums[i], 0) + 1);
		}
		
		System.out.println(ans);
		
		List<Map.Entry<Integer, Integer>> entryList = new ArrayList<>(ans.entrySet());
		
		entryList.sort(Map.Entry.comparingByValue(Comparator.reverseOrder()));

        List<Map.Entry<Integer, Integer>> firstKEntries = entryList.subList(0, Math.min(k, entryList.size()));
        
        System.out.println(firstKEntries);
        
        int[] answer = new int[k];
        for (int i = 0; i < k; i++) {
           answer[i] = firstKEntries.get(i).getKey();
        }
        
        return answer;  
    }
	
}
