from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """Graph traversal, back tracking"""
        def dfs_find(dividend, target, acc_product):
            if dividend == target:
                return acc_product

            visited.add(dividend)
            
            for neighbor, value in graph[dividend].items():
                if neighbor not in visited:
                    res = dfs_find(neighbor, target, acc_product * value)
                    if res != -1.0:
                        return res

            return -1.0

        # 1. build the graph
        graph = defaultdict(dict)

        for i, val in values:
            dividend, divisor = equations[i]
            graph[dividend][divisor] = val
            graph[divisor][dividend] = 1 / val

        # 2. Traverse the queries and find the division/product
        result = []
        res = -1.0
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                res = -1.0
            else:
                visited = set()
                res = dfs_find(dividend, divisor, 1.0)
            result.append(res)
        print(result)
        return result

eq1 = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
val1 = [3.0,4.0,5.0,6.0]
que1 = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]

eq2 = [["a","b"],["b","c"],["bc","cd"]]
val2 = [1.5,2.5,5.0]
que2 = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]

eq3 =[["a","b"]]
val3 = [0.5]
que3 = [["a","b"],["b","a"],["a","c"],["x","y"]]

s1 = Solution()
s1.calcEquation(eq1, val1, que1)

a = """
    1. When dividend exists, but divisor doesn't exist
    2. Create a dictionary of dictionary instead of dict of list
    3. Another tricky part is make sense of what to put in visit set, when to add, check and remove an element
        Why adding dividend into visited, not the pair (dividend, divisor)?
    """