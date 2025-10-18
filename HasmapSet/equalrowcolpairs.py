from typing import List
from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        res = 0

        rowTuples = Counter(tuple(row) for row in grid)
        for j in range(n):
            colTuples = tuple(grid[i][j] for i in range(n))
            res += rowTuples[colTuples] 

        return res 
    
sol = Solution()

print(sol.equalPairs([[3,2,1],[1,7,6],[2,7,7]]))