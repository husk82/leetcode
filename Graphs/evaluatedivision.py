from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for i, (Ai, Bi) in enumerate(equations):
            if Ai not in graph:
                graph[Ai] = []
            if Bi not in graph:
                graph[Bi] = []
            graph[Ai].append((Bi, values[i]))
            graph[Bi].append((Ai, 1/values[i]))
        
        def dfs(cur, tar, visited, product):
            if cur == tar:
                return product
            visited.add(cur)
            for neigh, value in graph[cur]:
                if neigh not in visited:
                    res = dfs(neigh, tar, visited, product*value)
                    if res != -1:
                        return res
            return -1

        res = []
        for Cj, Dj in queries:
            if Cj not in graph or Dj not in graph:
                res.append(-1)
            elif Cj == Dj:
                res.append(1)
            else:
                visited = set()
                res.append(dfs(Cj, Dj, visited, 1))
            
        return res
                



