# Definition for a binary tree node.
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        # 1. build the tree into a graph
        # 2. gather all leaves in a set
        # 3. run BFS on the leaf nodes
        def dfs(node: TreeNode) -> None:
            if not node:
                return 
            if not node.left and not node.right:
                leaves.add(node)
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
            dfs(node.left)
            dfs(node.right)


        graph = defaultdict(list)
        leaves = set()
        visited = set()
        queue = deque([leaves])
        ans = 0
        
        # run bfs on the leaves
        while queue:
            cur_dis = 1
            node = queue.pop()
            visited.add(node)

            for neighbor in graph[node] and neighbor not in visited:
                if cur_dis > distance:
                    break
                if neighbor in leaves:
                    ans += 1
                
                cur_dis += 1
                queue.append(neighbor)

        return ans // 2