from tree import TreeNode, Tree
from tree_traversal import Traversal

def cmp(a: int, b: int) -> int:
    return (a > b) - (a < b)

arr1 = [3, 9, 20, 8, 10, 15, 21, 7]
arr2 = [3, 9, 20, None, None, 15, 7]

# tree = TreeNode(3)
# tree.left = TreeNode(9)
# tree.right = TreeNode(20)
# tree.right.left = TreeNode(15)
# tree.right.right = TreeNode(7)

s1 = Traversal()
t1 = Tree()

# sorted_tree = t1.array_to_bst(root)
# s1.dfs_preorder(sorted_tree)

tree_object = t1.array_to_tree(arr1)
s1.dfs_preorder(tree_object)