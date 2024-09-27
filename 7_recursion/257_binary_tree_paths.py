from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, path):
            if not node:
                return path
            if not node.left and not node.right:
                path += str(node.val)
                result.append(path)
                return path
            
            path += str(node.val) + "->"
            dfs(node.left, path)
            dfs(node.right, path)

        result = []
        dfs(root, "")
        return result

s1 = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
s1.binaryTreePaths(root)
