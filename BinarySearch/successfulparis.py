from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        res = []

        for s in spells:
            low = 0
            high = m - 1
            mid = 0

            while low <= high:
                required = (success + s -1) // s
                mid = (low + high) // 2
                if potions[mid] < required:
                    low = mid + 1
                elif potions[mid] >= required:
                    high = mid - 1
                
            res.append(m-low)

        return res