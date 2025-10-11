from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        spots = 0
        empty = 0

        if n == 0:
            return True
        
        flowerbed = [0] + flowerbed + [0]

        for i in range (0, len(flowerbed)):
            if flowerbed[i] == 0:
                empty += 1
            else:
                empty = 0
            if empty == 3:
                empty = 1
                spots += 1
        return n <= spots

sol = Solution()

print(sol.canPlaceFlowers([1,0,0,0,0,0,1], 2))  # Expect true


"""
def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        spots = 0
        plots = len(flowerbed)
        i = 2

        if n == 0:
            return True
        
        if plots == 1 and n == 1:
            return flowerbed[0] == 0 

        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            spots += 1

        while i <= plots-1:
            if i+1 < plots and flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0: 
                spots += 1
                flowerbed[i] = 1
            i += 1
        if flowerbed[plots-1] == 0 and flowerbed[plots-2] == 0:
            spots += 1
        return spots >= n
"""