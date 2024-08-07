# Tree

## Traversal
### Preorder traversal
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