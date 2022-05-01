class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in num:
                return [num[diff], i]
            num[n] = i