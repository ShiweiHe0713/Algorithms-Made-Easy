# Back tracking
**Table of Contents**
- [Back tracking](#back-tracking)
  - [Probelms](#probelms)
    - [Basics](#basics)
      - [256 Binary tree paths](#256-binary-tree-paths)
      - [To find permutations/combinations](#to-find-permutationscombinations)


## Probelms
### Basics
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