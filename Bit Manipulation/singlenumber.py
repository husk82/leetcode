from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res 

# Create an instance
sol = Solution()

# Test cases
assert sol.singleNumber([2, 2, 1]) == 1, "Test case 1 failed"
assert sol.singleNumber([4, 1, 2, 1, 2]) == 4, "Test case 2 failed"
assert sol.singleNumber([1]) == 1, "Test case 3 failed"
assert sol.singleNumber([-1, -1, -2]) == -2, "Test case 4 failed"
assert sol.singleNumber([0, 1, 0]) == 1, "Test case 5 failed"

print("✅ All basic tests passed!")