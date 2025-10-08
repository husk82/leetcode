import java.util.*;

public class carFleet853 {
	
	public static void main (String[] args) {
		
		System.out.println(carFleet(12, new int [] {10,8,0,5,3}, new int [] {2,4,1,1,3}));
		
	}
	
	public static int carFleet(int target, int[] position, int[] speed) {
		
		Map<Integer, Integer> map = new TreeMap<>(Comparator.reverseOrder());
		
		for (int i=0; i<position.length; i++) {
			map.put(position[i], speed[i]);
		}
		
		double prevTime = -1.0;
		int fleet = 0;
		
		for (int key: map.keySet()) {
			double reachTime = (double) (target - key) / map.get(key);
			if (reachTime > prevTime) {
				fleet++;
				prevTime = reachTime;
			}
					
		}
		
		return fleet;
	}
	
}
