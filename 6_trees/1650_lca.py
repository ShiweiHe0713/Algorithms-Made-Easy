from tree import TreeNode, Tree
import tree_traversal

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
    a, b = p, q

    # Traverse upwards until both pointers meet
    while a != b:
        # a = a.parent if a else q
        # b = b.parent if b else p
        if a:
            a = a.parent
        else:
            a = q

        if b:
            b = b.parent
        else:
            b = p

    return a

# Example usage
root = TreeNode(3)
p = TreeNode(5)
q = TreeNode(1)
p.parent = root
q.parent = root
root.left = p
root.right = q