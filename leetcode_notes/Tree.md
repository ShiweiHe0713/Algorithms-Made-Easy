# Trees

1. **Basic operatsions**
   1. Delete, insert, find, change values
2. **Traversals**
   1. Traversal orders: In-order, pre-order, post-order, level-order, vertical-order
   2. Traversal methods: DFS, BFS, Backtracking
3. **Find paths**
4. **Find level**
5. **Find target**
   - Successor, predecessor
   - Ancestor
6. **Cycle detection**

6. **BST**
7. **Balanced Tree**



## Basic operations



## Traversal

### Traversal approach

#### DFS

#### BFS

##### Level-order

For the level-order traversal, we will have to find a way to mark the end of the each level. Commonly, we will have these approach:

1. Use two queues
2. Use a sentinel node
3. Store the length of each level

**For example, [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)**

**Very fundamental question about how to traverse the tree level by level.** We can solve it by :

1. Adding sentinel node to mark the end of each level
2. Use two queue to pop and append alternatively
3. Record the length of every level



##### Vertical-order



### Traversal orders

#### Preorder

[144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/description/)
Don't return the preorder result list, it's not recommended. Just modified the preorder list in the dfs body.

[606. Construct String from Binary Tree](https://leetcode.com/problems/construct-string-from-binary-tree/description/)
I have fallen into some traps for this quesiton:
1. Didn't include recursive calls in a recursion function body
2. Include unneccessary `()` around root.val while I shouldn't, because the root can be parent node's children, so the `()` is included already.
3. I enumerate every possible case in the recursion function body while some can be merged into a more general cases.

**How to use sorted and lambda function**
```python
sort_sq = lambda x : x * x
array = [-1,2,-3,4,-5,6]
print(sorted(array, key=sort_sq))
# [-1, 2, -3, 4, -5, 6]
print(sorted(ll.items(), key=lambda x : x[1][0]))
# [(14, [1, 5]), (1, (2, 6)), (3, (14, 5))]
print(sorted(ll.items(), key=lambda x : x[1][1]))
# [(3, (14, 5)), (14, [1, 5]), (1, (2, 6))]
```

**List comprehenstion**
```python
[columnTable[x] for x in sorted(columnTable.keys())]
```



#### Inorder

[94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)



## Find Paths

[437. Path Sum III](https://leetcode.com/problems/path-sum-iii/)

Prefix sum + pre-order traversal





## Find levels





## Find target

Find target always involves setting a global `self.result`. Depends on the problem, but most of the cases, we will only update `self.result` when we first encounter it which means `if condition == True and self.result is None`, then we will update it to avoid re-update the value to incorrect ones.



## Cycle detection





## BST

[530. Minimum Absolute Difference in BST](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)

- Use inorder to make the best of the sorted attributed of a BST
- Use a `prev` pointer to keep track of the last visited node. **For example, the largest node on the right side of a BST is not simply its left child, it should be the rightmost node in its left subtree.**



[230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

**In a BST or tree, the number of nodes in the tree is `n` , the `k` is the smallest number index, `h` is the height of the tree.**

- O(h) can be O(n) or O(logn), depend on whether the BST is balanced or not. So O(h) always describe the height of the tree even when it's very skewed, so using O(h) to describe the worst complexity is correct.



