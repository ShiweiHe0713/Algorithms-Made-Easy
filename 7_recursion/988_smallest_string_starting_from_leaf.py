from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node: Optional[TreeNode], cur_str: str) -> None:
            if not node:
                return 

            nonlocal min_str
            cur_str += chr(node.val + ord('a'))
            if not node.left and not node.right:
                # Reverse the string and compare with min_str
                cur_str = cur_str[::-1]
                if cur_str < min_str:
                    min_str = cur_str
            dfs(node.left, cur_str)
            dfs(node.right, cur_str)
            cur_str = cur_str[:-1]
        
        min_str = "z" * 8500
        dfs(root, "")
        return min_str