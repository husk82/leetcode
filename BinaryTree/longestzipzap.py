from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.long = 0
        def dfs(node: Optional[TreeNode], direction, count):
            if not node:
                return 
            if direction == "left":
                dfs(node.left, "left", 1)
                dfs(node.right, "right", count+1)
            if direction == "right":
                dfs(node.right, "right", 1)
                dfs(node.left, "left", count+1)
            self.long  = max(self.long, count)
        dfs(root.left, "left", 1)
        dfs(root.right, "right", 1)
        return self.long 


