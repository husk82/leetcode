class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i, n in enumerate(nums):
            if i > 0 and nums[i-1] == n:
                continue
            left, right = i+1, len(nums) - 1
            while left < right:
                if (nums[i] + nums[left] + nums[right]) > 0:
                    right -= 1
                elif (nums[i] + nums[left] + nums[right]) < 0:
                    left += 1 
                elif (nums[i] + nums[left] + nums[right]) == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result
        