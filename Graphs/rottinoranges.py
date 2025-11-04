from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottens = deque()
        visited = set()
        time = 0 
        fresh = 0
        m,n = len(grid), len(grid[0])
        for r in range (m):
            for c in range (n):
                if grid[r][c] == 2:
                    rottens.append((r,c,0))
                    visited.add((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while rottens:
            r, c, time = rottens.popleft()

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        rottens.append((nr, nc, time+1))
                
        return time if fresh == 0 else -1
                    
                    

        