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

In [285. Inorder Successor in BST](https://leetcode.com/problems/inorder-successor-in-bst/), to keep track of the predecessor, we can:

1. Use a global variable `self.prev` to keep track of it
2. Or use find_succ(node.left, prev_node=node)

## Cycle detection





## BST

- Checking BST is always compare prev and succ, not left and right

[530. Minimum Absolute Difference in BST](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)

- Use inorder to make the best of the sorted attributed of a BST
- Use a `prev` pointer to keep track of the last visited node. **For example, the largest node on the right side of a BST is not simply its left child, it should be the rightmost node in its left subtree.**



[230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

**In a BST or tree, the number of nodes in the tree is `n` , the `k` is the smallest number index, `h` is the height of the tree.**

- O(h) can be O(n) or O(logn), depend on whether the BST is balanced or not. So O(h) always describe the height of the tree even when it's very skewed, so using O(h) to describe the worst complexity is correct.





## Choice of BFS or DFS

### **When to Use BFS in Trees**

1. **Level-Order Traversal**
   - **Problem**: [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
   - **Problem**: [107. Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)

2. **Finding the Minimum Depth**
   - **Problem**: [111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

3. **Zigzag Level Order Traversal**
   - **Problem**: [103. Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)

4. **Cousins in a Binary Tree**
   - **Problem**: [993. Cousins in Binary Tree](https://leetcode.com/problems/cousins-in-binary-tree/)

### **When to Use DFS in Trees**

1. **In-Order, Pre-Order, and Post-Order Traversal**
   - **Problem**: [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
   - **Problem**: [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)
   - **Problem**: [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)

2. **Path Sum Problems (checking or finding specific paths)**
   - **Problem**: [112. Path Sum](https://leetcode.com/problems/path-sum/)
   - **Problem**: [113. Path Sum II](https://leetcode.com/problems/path-sum-ii/)

3. **Maximum Depth or Diameter Calculation**
   - **Problem**: [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
   - **Problem**: [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)

4. **Finding Nodes at a Certain Distance (like "K Distance" problems)**
   - **Problem**: [863. All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)

### **When Either BFS or DFS Can Be Used in Trees**

1. **Counting Nodes in a Complete Tree**
   - **Problem**: [222. Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/)

2. **Finding the Lowest Common Ancestor (Depending on Tree Properties)**
   - **Problem**: [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)
   - **Problem**: [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

3. **Symmetric Tree Check**
   - **Problem**: [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)

4. **Balanced Tree Check**
   - **Problem**: [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)
