from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """T: O(n), S: O(n)"""
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

    def isBalanced_I(self, root: Optional[TreeNode]) -> bool:
        """T: O(n^2)(worst case), O(nlogn), S: O(n)"""
        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return -1

            return 1 + max(height(node.left), height(node.right))
        
        if not root:
            return True
        if abs(height(root.left) - height(root.right)) >= 2:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right) 

    def isBalanced_II(self, root: Optional[TreeNode]) -> bool:
        """T: O(n), S: O(n)"""
        def helper(node: Optional[TreeNode]) -> (int, bool):
            if not node:
                return (-1, True)

            left_h, left_balanced = helper(node.left)
            if not left_balanced:
                return left_h, False
                
            right_h, right_balanced = helper(node.right)
            if not right_balanced:
                return right_h, False

            height = 1 + max(left_h, right_h)
            balanced = abs(left_h - right_h) < 2
            
            return (height, balanced)
        
        return helper(root)[1]

        