from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')

        for i in range (0, len(nums)):
            if (nums[i] < first):
                first = nums[i]
            elif (nums[i] > first and nums[i] < second):
                second = nums[i]
            
            if (nums[i] > second):
                return True
        
        return False

            


sol = Solution()

print(sol.increasingTriplet([5,1,6]))