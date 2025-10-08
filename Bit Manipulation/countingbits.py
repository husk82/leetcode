from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        for i in range (1, n+1):
            res[i] = res[i & (i - 1)] + 1
        return res

# Create an instance of your solution class
sol = Solution()

# Test cases
assert sol.countBits(0) == [0], "Test case 0 failed"
assert sol.countBits(2) == [0, 1, 1], "Test case 2 failed"
assert sol.countBits(5) == [0, 1, 1, 2, 1, 2], "Test case 5 failed"

print("All basic tests passed!")
