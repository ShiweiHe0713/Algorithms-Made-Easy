# Sliding Window

In [1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](./1438_longest_continuous_subarray_with_absolute_diff_less_than_or_equal_to_limit.py), it is keep expanding the right pointer, using both max and min heap/queue to keep track of the cur_max and cur_min. If the cur_max - cur_min exceed the limit, we will going to move the left pointer and pop elements from min/max heap until the limit is satisfied again. We can retract right pointer or let left directly jump to right + 1 when encounter a invalid subarray, since that way we could miss potential valid subarrays.

[121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lowest = prices[0]

        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        
        return res
    
```
In this sliding window problem, we only need two variables: one to keep track of the current maximal profit, the second is the lowest price so far. In a bruteforce way, we have to use two loops, the first traverse the whole prices array, the second will find the highest prices after the current anchor, result in a time complexity `O(n^2)`. Here comes the idea of sliding window to avoid multiple loops.

We don't have to have the second loop to forwardly check the highest price. Instead, we only take care of the max profit up until the current index by comparing the lowest traversed before and the current price. In this way by looking backward, we make use of the elements we already visited to save more time.

In conclusion, we will have a slower left pointer that will keep track of the lowest price, and a keep-moving pointer on the right to compare the current max profit with the difference between current element and the lowest. 
