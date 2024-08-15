# Array, string, and Hashing

 Hashmap/ Hashset题目：
        Leetcode 1. Two Sum
        Leetcode 146. LRU Cache (Python中可以使用OrderedDict来代替)
        Leetcode 128. Longest Consecutive Sequence
        Leetcode 73. Set Matrix Zeroes
        Leetcode 380. Insert Delete GetRandom O(1)
        Leetcode 49. Group Anagrams
        Leetcode 350. Intersection of Two Arrays II
        Leetcode 299. Bulls and Cows
        Leetcode 348 Design Tic-Tac-Toe

**在要用到Hashmap存number or strings的时候，一定要注意是否有重复元素，然后区分Value应该是array还是int/string。**

In [506 Relative Ranks](./506_relative_ranks.py), the index mapping is very confusing, taking a lot of time to wrap my head around. 
For the original array `score`, we have the score and its corresponding index. 


In [128 Longest Consecutive Subsequence](./128_longest_consecutive_subsequence.py), only continue the for loop if the number is the start of a sequence, otherwise skip. And use a while loop for the start of the array, update the max_result each while process.
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        max_result = 0

        for num in nums:
            # number is the start of a sequence
            if num - 1 not in num_set:
                result = 1
                while num + 1 in num_set:
                    num += 1
                    result += 1
                max_result = max(result, max_result)
            
        return max_result
```