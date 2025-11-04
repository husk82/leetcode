import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.current = 1
        self.heap = []

    def popSmallest(self) -> int:
        if not self.heap:
            self.current += 1
            return self.current - 1
        else:
            return heapq.heappop(self.heap)
            

    def addBack(self, num: int) -> None:
        if self.current > num: 
            heapq.heappush(self.heap, num)
    