from collections import deque

class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        
        while self.queue[0] < t-3000 or self.queue[0] > t:
            self.queue.popleft() 
                
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

recentCounter = RecentCounter()


print(recentCounter.ping(1))      # expected output: 1
print(recentCounter.ping(100))    # expected output: 2
print(recentCounter.ping(3001))   # expected output: 3
print(recentCounter.ping(3002))   # expected output: 3

