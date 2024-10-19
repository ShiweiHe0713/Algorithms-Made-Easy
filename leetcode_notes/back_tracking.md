# Back tracking
**Table of Contents**
- [Back tracking](#back-tracking)
  - [Probelms](#probelms)
    - [Basics](#basics)
      - [256 Binary tree paths](#256-binary-tree-paths)
      - [To find permutations/combinations](#to-find-permutationscombinations)



## Probelms

#### [46. Permutations](https://leetcode.com/problems/permutations/)

#### [7. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

In this problem, the **runtime** we bill `the number of leaf nodes` x `the length of each path`, namely `O(4^n * n)`. Distinguish between the depth of the leaf node and the path length. And the reason why it's `4^n` but not `2^n` is that every node at worse can have 4 children(choices), and after we reach the valid leaf node, we have to append that path to our result array.

- Time complexity: $O(4^n \times n)$



#### [39. Combination Sum](https://leetcode.com/problems/combination-sum/)

In this problem, **the time complexity if different from last one**, since we're exploring every possibility even it's invalid. Let's say `n` is the length of `candidates`, `k` is target, and `m` is the smallest element in `candidates`, so we have:

- Time complexity: $O(n^{k/m})$ . Worst case, all the node in the tree is $n^{k/m + 1} - 1$ based on geometric series sum.
- Space: $O(k/m)$. When we use the smallest element to sum up to target, all of it will be added to the stack because of recursion.



#### [77. Combinations](https://leetcode.com/problems/combinations/)

- **Time complexity** for this problem is $O(\frac{n!}{(k-1)!(n-k)!})$
- **Space complexity** is $O(k)$, the numbers in stack is up bounded by the k.



#### [78. Subsets](https://leetcode.com/problems/subsets/)

- **Time complexity** for this problem is $O(n \times 2^n)$
- **Space complexity** is $O(n)$





#### [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)

- **Time complexity** for this problem is $O(\frac{4^n}{\sqrt{n}})$
- **Space complexity** is $O(n)$



#### [40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)

Purpose of `if i > start and candidates[i] == candidates[i - 1]: continue`:

This condition ensures that the algorithm **skips over duplicate values** but does so only **when iterating at the same level of recursion**. 

- **Time complexity** for this problem is 
- **Space complexity** is 



#### 256 Binary tree paths

In [257 binary tree paths](/back_tracking/257_binary_tree_paths.py), 
```python
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, path):
            if not node:
                return path
            if not node.left and not node.right:
                path += str(node.val)
                result.append(path)
                return path
            
            path += str(node.val) + "->"
            dfs(node.left, path)
            dfs(node.right, path)

        result = []
        dfs(root, "")
        return result
```
- why we we don't have to delete the string after the dfs calls in the body like what we did in [1219](/back_tracking/1219_path_with_maximum_gold.py)?
    Because we only append the string at the leaf node, there is no need to backtracking. We don't have to return anything to the root node.

- and why we don't have to delete the string after the dfs(node.left)?
    Because the `path` we pass into dfs(node.left, path) and dfs(node.right, path) is the same. The path passed into dfs(node.right, path) won't be modified by the path passed in dfs, it only acts like a formal argument.

In [113 Path Sum II](/back_tracking/113_path_sum_II.py), we have to return the **copy of an array instead**, otherwise the array is passed by reference and will be changed in the future potentially causing unwanted changes.
Once we enter the recursive funciton body, we either return or not. When it is the non-terminating case, we will append the element into the array and then doing other operations such as handling the leaf node, calling other dfs functions. **After these being done, we will pop the element out of the array to finish backtracking process.**

#### To find permutations/combinations
In [Combination of numbers](./combo_of_numbers.py), we will append to the `cur_arr` until we react the length of `n` which is the base case. After reach the base case, we will return the copy of the cur_arr(but we don't have to empty the arr, since we are going to backtracking popping elements from it.) 

```python
for i in range(10):
    # skip if having the k repetive elements
    if len(cur_arr) >= k and cur_arr[-k:]  == [i] * k:
        continue
    cur_arr.append(i)
    dfs(cur_arr)
    cur_arr.pop()
```
The `cur_arr[-k:]` means the last k elements in the array.

In [39. Combination sum](./39_combination_sum.py), in the for loop, we will have `start` as a recurision function argument, since we only want `i` to traverse from `start` to `n-1`. 
```python
for i in range(start, len(candidates)):
                arr.append(candidates[i])
                dfs(i, arr)
                arr.pop()
```
In order to not have duplicates like `[2,3,2]`and `[2,2,3]`(list is not hashable so we can't use a set). So we have to figure out how to avoid going back in backtracking. We introduce a `start` variable which is the start index in the `candidates` array, and we will only consider the elements of start or after starts. For example in `[2,3,5,7]` when `start` == 1, we only consider [3,5,7] in the for loop, and the dfs inside of for loop will only use these three numbers, won't go back to get 2, since all possibility related to 2 has been considered when `start` == 0;





## Runtime analysis