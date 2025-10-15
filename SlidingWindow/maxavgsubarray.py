from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        j = k-1
        maxSum = float('-inf')
        sum = 0
        length = len(nums)
        for l in range (i , j + 1):
                sum += nums[l]
        while j < length:    
            maxSum = max(maxSum, sum)
            if j+1 < length:
                sum = sum - nums[i] + nums[j+1] 
            i += 1
            j += 1     
        return maxSum/k
    
sol = Solution()

print(sol.findMaxAverage([1,12,-5,-6,50,3], 4))