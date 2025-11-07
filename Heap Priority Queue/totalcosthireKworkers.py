from typing import List
import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        left_candidates = costs[:candidates]
        right_candidates = costs[max(candidates, n-candidates):]
        left_index = candidates
        right_index = max(candidates, n-candidates) - 1
        
        heapq.heapify(left_candidates)
        heapq.heapify(right_candidates)
        
        total = 0

        for _ in range(k):
            if not right_candidates or (left_candidates and left_candidates[0] <= right_candidates[0]):
                total += heapq.heappop(left_candidates)
                if left_index <= right_index:
                    heapq.heappush(left_candidates, costs[left_index])
                    left_index += 1
            else:
                total += heapq.heappop(right_candidates)
                if left_index <= right_index:
                    heapq.heappush(right_candidates, costs[right_index])
                    right_index -= 1
                    
        return total