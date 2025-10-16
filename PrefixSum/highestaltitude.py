from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:  
        prefix = [0] * (len(gain) + 1)

        for i in range (1, len(gain)):
            prefix[i] = prefix[i-1] + gain[i] 
        print(prefix)
        return max(prefix)
    
sol = Solution()

print(sol.largestAltitude([-5,1,5,0,-7]))