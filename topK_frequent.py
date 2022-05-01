class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hset = {}
        for i in range(len(nums)):
            if nums[i] in hset:
                hset[nums[i]] = hset.get(nums[i]) + 1
            else:
                hset[nums[i]] = 1
        hset = sorted(hset, key=hset.get, reverse=True)
        return hset[:k]     