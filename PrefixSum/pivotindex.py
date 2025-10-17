from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        suffix = [0] * (n + 1)

        for i in range (0, n):
            prefix[i+1] = prefix[i] + nums[i]
        
        for i in range (n-1, -1, -1):
            suffix[i] = suffix[i+1] + nums[i]

        for i in range (n):
            if prefix[i] == suffix[i+1]:
                return i
        return -1
    
sol = Solution()

print(sol.pivotIndex([1,7,3,6,5,6]))