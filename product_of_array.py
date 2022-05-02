class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        aux = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            aux[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            aux[i] *= postfix
            postfix *= nums[i]
        return aux