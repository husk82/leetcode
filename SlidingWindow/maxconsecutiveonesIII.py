from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = j = maxLen = flip = 0

        while j < len(nums):
            if nums[j] == 0:
                flip += 1
            
            if flip <= k:
                maxLen = max(maxLen, j-i+1)
            else:
                while flip > k:
                    if nums[i] == 0:
                        flip -= 1
                    i += 1
            j += 1
        return maxLen