# Binary Search

## Binary search problem generalized

Binary search problems are always trying to find a value in some condition. 

**For example:**

- Find the **[ith largest/smallest]** element in **[a container]** that **[satisfies some condition]** .

- Find the **[minimal]** days **[that we can make `m` bouquet which require `k` adjacent bloomed flowers]**

- Find the **[smallest]** capacity **[that we can ship all the items within `days` days]**

- Find the **[smallest]** distance pair **[such that it is the Kth smallest distance pair ]**
- Find the **[Kth smallest]** number in a **[mult. matrix]**.  ([such that it's the Kth smallest])
  

## Template

```python
def binary_search():
  def condition(mid_vale):
		"""Return True if mid_value satisfy our condition(such as we ship ship at most n days with a capacity `mid`)"""
    count = something # usually 0 or 1 depends on the problem
    for loop to calculate the count;
    return True or False according to the requirement

  # explicitly handle the edge cases
  if something: return something

  l, r = something according to the value search range
  
  while l < r:
    mid = l + (r - l) // 2
    if condition(mid):
      r = mid
    else:
      l = mid + 1
    
   return l # or r
```

**The time complexity will be O(condition() * log(search range))**.



## Problems
- **[1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days)** 
- [719. Find K-th Smallest Pair Distance](https://leetcode.com/problems/find-k-th-smallest-pair-distance)  
- [1283. Find the Smallest Divisor Given a Threshold](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold)  
- [668. Kth Smallest Number in Multiplication Table](https://leetcode.com/problems/kth-smallest-number-in-multiplication-table)  
- [410. Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum)  
- [1482. Minimum Number of Days to Make m Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets)  
- **[153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array)**



**[540. Single Element in a Sorted Array](https://leetcode.com/problems/single-element-in-a-sorted-array/)**

**在这个binary search问题里，我们要向左还是向右搜寻的条件是哪边的长度是奇数。** 这一点可以通过任何一边的长度来判断，但是为了consistency，我决定一直用左边的长度来判断。还有一点要注意的是mid可能指向两个重复元素的第一个或者第二个，为了一致性，我们可以让mid永远指向第一个。



**In [1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)**:

In many medium binary search questions, we will often see two questions combine together. In this one, we will have **binary search and then a linear scan**. For me it was hard to think of using binary search to solve this problem but it's easy to implement. It's also hard for me to implement linear scan since I used a `while` loop, and the index always go wrong.

在Linear Scan中，先自增再比较或者先比较再自增，会出现包含当前元素和不包含的情况。

```python
def days_taken(capacity: int) -> int:
            total_weight = 0
            days = 1
      
            for weight in weights:
                if total_weight + weight > capacity:
                    days += 1
                    total_weight = 0
                total_weight += weight

            return days

```

这样写的好处就是：

1. 如果 total_weight + weight > capacity, 当前的weight就不会被加入上一个total_weight了
2. 应该是total_weight + weight > capacity，而不是 total_weight + weight >= capacity。因为小于和等于都是inclusive的合理状态，只有当大于的时候才是不合理状态。



Whether we return `l` or `r` as a result depends on how to end the while loop. For example, our termination will be l == r == mid, then our algorithm will go into if or else to either increase `l` or decrease `r` for the while loop to stop. And we are going to return the one that doesn't change at the last step.

In [162 Find peak element](./162_find_peak_element.py), we search to the right if nums[mid+1] > nums[mid], search the left if nums[mid-1] > nums[mid]. The reason why we do this is that binary search is about how to narrow down the searching scope, either to left or right. So the most important thing we need to worry about is whether go to left or right. Here if nums[mid-1] > nums[mid] means nums[mid] can't be the peak since it's smaller than its eneighbor. And since nums[mid-1] > nums[mid], nums[mid-1] could potentially be the peak or the element on its left side. Even though we can't exclude there're peaks on the right side of mid in this case, it is certian that there will be peal in the left side(Even if it's monotonic, out of boundary will be negative infinite.) So we have to write it in the certain way which is when nums[mid-1] > nums[mid], we go left by `r = mid - 1`. The same for the right side.



### Explicit Binary Search
- Leetcode 34. Find First and Last Position of Element in Sorted Array

- Leetcode 33. Search in Rotated Sorted Array

- Leetcode 1095. Find in Mountain Array

- [x] Leetcode 162. Find Peak Element

- Leetcode 278. First Bad Version

- Leetcode 74. Search a 2D Matrix

- Leetcode 240. Search a 2D Matrix II

  
### Implicit Binary Search
- Leetcode 69. Sqrt(x)
- Leetcode 540. Single Element in a Sorted Array
- Leetcode 644. Maximum Average Subarray II
- Leetcode 528. Random Pick with Weight
- Leetcode 1300. Sum of Mutated Array Closest to Target
- Leetcode 1060. Missing Element in Sorted Array
- Leetcode 1062. Longest Repeating Substring
- Leetcode 1891. Cutting Ribbons