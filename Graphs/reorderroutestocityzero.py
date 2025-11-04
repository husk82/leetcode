from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = {}
        for a,b in connections:
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append((b, True))
            graph[b].append((a, False))

        visited = set()
        count = 0
        def dfs(city):
            nonlocal count
            for neigh, needs_reverse in graph[city]:
                if neigh not in visited:
                    visited.add(neigh)
                    if needs_reverse:
                        count += 1
                    dfs(neigh)
        visited.add(0)
        dfs(0)
        return count
