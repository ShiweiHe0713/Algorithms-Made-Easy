class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(root) -> str:
            if not root:
                return ""
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            if not left and not right:
                return f"{root.val}"
            if not right:
                return f"{root.val}({left})"
            return f"{root.val}({left})({right})"
        
        return dfs(root)

    def tree2str_wrong1(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        def preorder(root: Optional[TreeNode]) -> None:
            if not root:
                return ""
            if not root.left and not root.right:
                return f"({root.val})"
            if not root.left and root.right:
                return f"({root.val}()({root.right.val}))"
            if root.left and not root.right:
                return f"({root.val}({root.left.val}))"
            else:
                return f"({root.val}({root.left.val})({root.right.val}))"
        
        result = f"{root.val}" + preorder(root.left) + preorder(root.right)
        return result
    
    def tree2str_not_good(self, root: Optional[TreeNode]) -> str:
            if not root:
                return ""
            def preorder(root: Optional[TreeNode]) -> None:
                if not root:
                    return ""
                if not root.left and not root.right:
                    return f"{root.val}"
                if not root.left and root.right:
                    return f"{root.val}()({preorder(root.right)})"
                if root.left and not root.right:
                    return f"{root.val}({preorder(root.left)})"
                else:
                    return f"{root.val}({preorder(root.left)})({preorder(root.right)})"
            
            return preorder(root)