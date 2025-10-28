from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, curMax: int): 
            if not node:
                return 0
            good = 1 if node.val >= curMax else 0
            curMax = max(curMax, node.val)
            good += dfs(node.left, curMax)
            good += dfs(node.right, curMax)
            
            return good
        return dfs(root, root.val) if root else 0