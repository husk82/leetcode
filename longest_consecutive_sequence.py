class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        aset = set(nums)
        longest = 0
        for i in aset:
            if (i-1) not in aset:
                length = 0
                while (i + length) in aset:
                    length += 1
                    
                longest = max(length, longest)
        return longest 