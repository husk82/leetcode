from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        mArea = 0

        while i < j:
            if height[i] < height[j]:
                mArea = max(mArea, height[i] * (j - i))
                i += 1
            else:
                mArea = max(mArea, height[j] * (j - i))
                j -= 1

        return mArea

sol = Solution()

print(sol.maxArea([1,8,6,2,5,4,8,3,7]))