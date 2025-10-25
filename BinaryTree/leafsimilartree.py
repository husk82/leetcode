from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1, leaves2 = [], []
        return self.findLeafNodes(root1, leaves1) == self.findLeafNodes(root2, leaves2)


    def findLeafNodes(self, root:Optional[TreeNode], leaves: list) -> list:
        if not root:
            return leaves
        if not root.left and not root.right:
            leaves.append(root.val)
            return leaves
        self.findLeafNodes(root.left, leaves)
        self.findLeafNodes(root.right, leaves)
        return leaves

        