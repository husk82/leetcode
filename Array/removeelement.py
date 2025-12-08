from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0 
        j = len(nums) - 1

        while i <= j:
            if nums[i] == val:
                while i < j and nums[j] == val:
                    j -= 1
                nums[i] = nums[j]
                j -= 1
            i += 1   

        return j + 1

sol = Solution()

print(sol.removeElement([0,1,2,2,3,0,4,2], 2))
print(sol.removeElement([3,2,2,3], 3))