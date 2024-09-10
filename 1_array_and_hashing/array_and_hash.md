# Array, string, and Hashing

## Problems

**在要用到Hashmap存number or strings的时候，一定要注意是否有重复元素，然后区分Value应该是array还是int/string。**

#### 506 Relative Ranks

In [506 Relative Ranks](./506_relative_ranks.py), the index mapping is very confusing, taking a lot of time to wrap my head around. 
For the original array `score`, we have the score and its corresponding index. 



#### 128 Longest Consecutive Subsequence

In [128 Longest Consecutive Subsequence](./128_longest_consecutive_subsequence.py), only continue the for loop if the number is the start of a sequence, otherwise skip. And use a while loop for the start of the array, update the max_result each while process.



#### [945. Minimum Increment to Make Array Unique](https://leetcode.com/problems/minimum-increment-to-make-array-unique/)

##### Sorting approach

In this [question](./945_Minimum_Increment_to_Make_Array_Unique.py), after sorting we only have to increment the elements smaller or equal to its previous one to `nums[i-1] + 1`. It's **making use of the sorted array attribute**. 

**But the question is if we increment the element to `nums[i-1]+1` how do we prove it's the minimum move?** 

Just picture an array of `[1,1,1,1,1]`, in order to move the minimal steps, we will increment each 1 to the last element plus 1, for the array to become `[1,2,3,4,5]`. 

If `nums[i]` is smaller than or equal to `nums[i-1]`, the minimal way to ensure uniqueness is to make `nums[i]` the smallest possible value that is still greater than `nums[i-1]`. The smallest such value is `nums[i-1] + 1`. Any larger increment would create unnecessary additional steps. Each move is the minimum required to ensure that every element is unique, and no excess increments are made.

#### Counting and carry over 

if any element has duplicates, we will carry over the extra duplicates to the next number, and make them only appear once. For example. For example, 

- we have two 1s, two 2s, and one 3. 
- First step will be one 1, three 2s, one 3s, 
- The next step is one 1, one 2, three 3s
- ...
- Become one 1, one 2, one 3, one 4, one 5

In an array and hashing problem, we have to pay attention to the size of the extra data structure we created. Whether the size of the input array or using the max num in the array as the length, what are the pros and cons. For example, we have: [1,1,1,1,1,1], [1,100000]. If we use the max number be the size of the array for the latter, it will be large since it is very sparse. 



## Hashmap/ Hashset题目：
​        Leetcode 1. Two Sum
​        Leetcode 146. LRU Cache (Python中可以使用OrderedDict来代替)
​        Leetcode 128. Longest Consecutive Sequence
​        Leetcode 73. Set Matrix Zeroes
​        Leetcode 380. Insert Delete GetRandom O(1)
​        Leetcode 49. Group Anagrams
​        Leetcode 350. Intersection of Two Arrays II
​        Leetcode 299. Bulls and Cows
​        Leetcode 348 Design Tic-Tac-Toe