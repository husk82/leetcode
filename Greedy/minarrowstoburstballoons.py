from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        arrows = 1
        prev_end = points[0][1]
        print(points)
        for i in range (1, len(points)):
            if prev_end < points[i][0]:
                arrows += 1
                prev_end = points[i][1]
        return arrows

sol = Solution()
print(sol.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))