# PQ & Heap

## Conclusion

**Priority queue and heaps are always used to solve greedy problems, involving design a self-sorting method.**



## Time complexity

In short, let's say we have `n` elements, the time complexities of priority queues are:

| Operation         | Time Complexity |
| ----------------- | --------------- |
| Heapify           | O(n)            |
| push (Insert)     | O(log n)        |
| pop (Extract_max) | O(log n)        |
| Find_max          | O(1)            |
| Find_2nd_max      | O(1)            |
| Extract_2nd_max   | O(log n)        |

- Push is achieved by: First push to the leaf and then **buble up**
- Pop is swapping root with last element, and delete last element, then **bubble down** the root



**In [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)** and **[621. Task Scheduler](https://leetcode.com/problems/task-scheduler/)**, we can see some similarity: We want to always choose the largest or smallest element, so there's an order maintain unchanged. In meeting rooms II we always want to find the earliest end time in the heap, in task scheduler we always want to find the task with the highest frequency in order to make decisions with the next steps. So the sorting property is always maintained, if we want to constantly and dynamically get the largest or smallest element, we could use heap.



#### [658. Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/)

The error you're encountering (`"< operator is not supported between Element and Element"`) arises because the `heapq` module in Python relies on the `__lt__` (less than) method to compare elements when creating a heap. By default, `heapq` uses the `<` operator to organize elements, so even if you define `__ge__` or `__gt__`, it still expects `__lt__` to be present.





## Problems

### K Elements (Max/Min Heaps)
[973. K Closest Points]
[347. Top k Largest Elements]
[692. Top K Frequent Words] 
[378. Kth Smallest Element in a Sorted Matrix]



### Merging and Sorting
[23. Merge K Sorted Lists]
[88. Merge Sorted Arrays] 



### Frequency and Counting Problems (Heap or Custom Data Structures)
[895. Maximum Frequency Stack ]
[767. Reorganize String]



### Data Stream or Sliding Window (Heaps or Balanced Structures)
[295. Find Median from Data Stream]
[1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit]



### Miscellaneous or Specialized Heap/Queue
[264. Ugly Number II]
[1086. High Five]

