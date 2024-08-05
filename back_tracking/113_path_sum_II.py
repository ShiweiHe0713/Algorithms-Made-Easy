from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node: Optional[TreeNode], arr: List[int], cur_sum: int):
            if not node:
                return
            cur_sum += node.val
            arr.append(node.val)
            if not node.left and not node.right:
                # We will append and return at here
                if cur_sum == targetSum:
                    result.append(arr.copy())
                arr.pop()
                return    
            
            dfs(node.left, arr, cur_sum)
            dfs(node.right, arr, cur_sum)
            arr.pop()

        result = []
        dfs(root, [], 0)
        print(result)
        return result
    
root1 = TreeNode(0)
root1.left = TreeNode(1)
root1.right = TreeNode(1)
s1 = Solution()
s1.pathSum(root1, 1)