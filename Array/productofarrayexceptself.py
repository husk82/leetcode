from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [0] * length
        suffix = [0] * length     
        result = [0] * length

        prefix[0] = 1
        for i in range (1, length):         
            prefix[i] = prefix[i-1] * nums[i-1]
        print(prefix);

        suffix[length - 1] = 1
        for i in range (length-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        print(suffix);
        for i in range (0, length):
            result[i] = prefix[i] * suffix[i]
        return result

sol = Solution()

print(sol.productExceptSelf([1,2,3,4,5]))