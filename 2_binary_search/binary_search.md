# Binary Search

Whether we return `l` or `r` as a result depends on how to end the while loop. For example, our termination will be l == r == mid, then our algorithm will go into if or else to either increase `l` or decrease `r` for the while loop to stop. And we are going to return the one that doesn't change at the last step.

In [162 Find peak element](./162_find_peak_element.py), we search to the right if nums[mid+1] > nums[mid], search the left if nums[mid-1] > nums[mid]. The reason why we do this is that binary search is about how to narrow down the searching scope, either to left or right. So the most important thing we need to worry about is whether go to left or right. Here if nums[mid-1] > nums[mid] means nums[mid] can't be the peak since it's smaller than its eneighbor. And since nums[mid-1] > nums[mid], nums[mid-1] could potentially be the peak or the element on its left side. Even though we can't exclude there're peaks on the right side of mid in this case, it is certian that there will be peal in the left side(Even if it's monotonic, out of boundary will be negative infinite.) So we have to write it in the certain way which is when nums[mid-1] > nums[mid], we go left by `r = mid - 1`. The same for the right side.

## Problems
基础知识：二分法是用来解法基本模板，时间复杂度logN；常见的二分法题目可以分为两大类，显式与隐式，即是否能从字面上一眼看出二分法的特点：要查找的数据是否可以分为两部分，前半部分为X，后半部分为O
### Explicit Binary Search
- Leetcode 34. Find First and Last Position of Element in Sorted Array
- Leetcode 33. Search in Rotated Sorted Array
- Leetcode 1095. Find in Mountain Array
- [x] Leetcode 162. Find Peak Element
- Leetcode 278. First Bad Version
- Leetcode 74. Search a 2D Matrix
- Leetcode 240. Search a 2D Matrix II
- 
### Implicit Binary Search
- Leetcode 69. Sqrt(x)
- Leetcode 540. Single Element in a Sorted Array
- Leetcode 644. Maximum Average Subarray II
- Leetcode 528. Random Pick with Weight
- Leetcode 1300. Sum of Mutated Array Closest to Target
- Leetcode 1060. Missing Element in Sorted Array
- Leetcode 1062. Longest Repeating Substring
- Leetcode 1891. Cutting Ribbons