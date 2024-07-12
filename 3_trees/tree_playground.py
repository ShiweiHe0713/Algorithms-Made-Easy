from tree_node import TreeNode
from tree_traversal import Traversal

def cmp(a: int, b: int) -> int:
    return (a > b) - (a < b)

root = [3, 9, 20, 8, 10, 15, 21, 7]

Tree = TreeNode(3)
Tree.left = TreeNode(9)
Tree.right = TreeNode(20)
Tree.right.left = TreeNode(15)
Tree.right.right = TreeNode(7)

s1 = Traversal()
s1.dfs_preorder(Tree)

