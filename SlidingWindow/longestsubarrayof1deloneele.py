from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = r = 0
        zero = 0
        maxOnes = 0
        while r < len(nums):
            if nums[r] == 0:
                zero += 1
            if zero <= 1:
                maxOnes = max(maxOnes, r - l)
            else:
                while zero > 1:
                    if nums[l] == 0:
                        zero -= 1
                    l += 1
            r += 1
        return maxOnes