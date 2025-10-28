from typing import Optional
from collections import defaultdict
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        self.count = 0

        def dfs(node, curSum):
            if not node:
                return 
            
            curSum += node.val
            self.count += prefix[curSum - targetSum]

            prefix[curSum] += 1

            dfs(node.left, curSum)
            dfs(node.right, curSum)

            prefix[curSum] -= 1
        dfs(root, 0)
        return self.count

        