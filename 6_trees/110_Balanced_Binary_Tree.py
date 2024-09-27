from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node) -> int:
            nonlocal flag
            if not node:
                return 0

            left_h = dfs(node.left)
            right_h = dfs(node.right)
            
            if abs(left_h - right_h) > 1:
                flag = False
                
            return 1 + max(left_h, right_h)

        flag = True
        dfs(root)
        return flag