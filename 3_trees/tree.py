from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    # def __init__(self, root: List[int]) -> Optional[TreeNode]:
    #     """Level-order array to Tree"""
    #     pass
    
    def array_to_tree(self, array: List[int]) -> Optional[TreeNode]:
        if not array:
            return None
        
        root = TreeNode(array[0])
        queue = [root]
        i = 1
        
        while i < len(array):
            current = queue.pop(0)
            
            if i < len(array) and array[i] is not None:
                current.left = TreeNode(array[i])
                queue.append(current.left)
            i += 1
            
            if i < len(array) and array[i] is not None:
                current.right = TreeNode(array[i])
                queue.append(current.right)
            i += 1
        
        return root


    def array_to_bst(self, array: List[int]) -> Optional[TreeNode]:

        def binary_search_build(array: List[int]) -> Optional[TreeNode]:
            if not array:
                return
            mid = len(array) // 2
            root = TreeNode(array[mid])
            root.left = binary_search_build(array[:mid])
            root.right = binary_search_build(array[mid+1:])
            return root
        
        array.sort()
        result = binary_search_build(array)
        return result