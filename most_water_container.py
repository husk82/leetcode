class Solution:
    def maxArea(self, height) -> int:
        l, r = 0, len(height) - 1
        area = 0
        width = len(height) - 1
        while l < r:
            min_height = min(height[l], height[r])
            current_area =  min_height * width
            area = max(current_area, area) 
            if height[l] < height[r]:
                l += 1
                width -= 1
            else:
                r -= 1
                width -= 1
        return area

