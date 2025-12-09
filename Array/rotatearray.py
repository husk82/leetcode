from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        n = len(nums)
        if k == n:
            return
        new = [0] * n
        for i in range (0, n):
            new[(i+k)%n] = nums[i]

        nums[:] = new
        """
        k %= len(nums)

        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])