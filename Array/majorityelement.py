from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        cur = nums[0]
        for num in nums:
            if cur == num:
                count += 1
            else:
                count -= 1
            if count == 0:
                cur = num
                count += 1
        return cur 