from typing import Optional
from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        
        queue = deque([(root, 1)])
        lvlSum = {}

        while queue:
            node, lvl = queue.popleft()
            
            lvlSum[lvl] = lvlSum.get(lvl, 0) + node.val
            
            if node.left:
                queue.append((node.left, lvl+1))
            if node.right:
                queue.append((node.right, lvl+1))
            
        return max(lvlSum, key=lvlSum.get)



