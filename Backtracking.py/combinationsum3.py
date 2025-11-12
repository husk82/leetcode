from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k == 0 or n == 0:
            return []
        res = []
        def backtrack(start, path, total):
            if total == n and len(path) == k:
                res.append(path)
                return
            if total > n or len(path) > k:
                return
            
            for i in range (start, 10):
                backtrack(i+1, path + [i], total+i)

        backtrack(1,[],0)

        return res