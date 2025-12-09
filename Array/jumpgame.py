from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = nums[0]
        for i in range (1, len(nums)):
            if i > farthest:
                return False
            else:
                farthest = max(farthest, i + nums[i])
            
        return farthest >= len(nums) - 1
