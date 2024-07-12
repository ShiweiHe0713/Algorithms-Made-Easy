from typing import Optional, List
from tree import TreeNode, Tree

# dfs, bfs, preorder, inorder, postorder

class Traversal:
    def dfs_preorder(self, root: Optional[TreeNode]) -> List[int]:        
        """144. Binary Tree Preorder Traversal"""
        def dfs(root: Optional[TreeNode]) -> None:
            if not root:
                return 
            preorder.append(root.val)
            print(root.val)
            dfs(root.left)
            dfs(root.right)
        
        preorder = []
        dfs(root)
        return preorder

    def bfs_preorder(self, root: Optional[TreeNode]) -> List[int]:
        """Preorder"""
        result = []
        stack = [root]
        while stack:
            cur = stack.pop()
            result.append(cur.val)

            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        print(result)
        return result
    
