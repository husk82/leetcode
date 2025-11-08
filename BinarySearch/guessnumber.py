# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0


class Solution:
    def guess(self, num: int) -> int:
        #NEEDS TO BE WRITTEN
        return
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        mid = (low + high)//2
        
        while self.guess(mid) != 0:
            if self.guess(mid) == -1:
                high = mid - 1
                mid = (high + low) // 2
            elif self.guess(mid) == 1:
                low = mid + 1
                mid = (low + high) // 2
        
        return mid
                
        