from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = j = 0 
        if (len(nums) == 1):
            return
        
        while i < len(nums) and j < len(nums):
            if nums[j] == 0 and nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            if nums[j] != 0 and nums[i] == 0:
                j = i
            i += 1
        return nums
    
sol = Solution()

print(sol.moveZeroes([4,2,4,0,0,3,0,5,1,0]))
