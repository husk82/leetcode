from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        skipped = 0
        intervals.sort(key=lambda x:x[1])
        pre_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < pre_end:
                skipped += 1
            else:
                pre_end = intervals[i][1]
        return skipped 
