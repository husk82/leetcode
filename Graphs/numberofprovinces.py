from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        number_of_cities = len(isConnected)
        def dfs(city):
            for c in range(number_of_cities):
                if city != c and isConnected[city][c] == 1 and c not in visited:
                    visited.add(c)
                    dfs(c)
            
        province = 0
        for city in range(number_of_cities):
            if city not in visited:
                visited.add(city)
                dfs(city)
                province += 1
        
        return province