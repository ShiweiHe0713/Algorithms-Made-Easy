# Sorting
*Some conclusion*
| Sorting        |   Time   |
| ------------   | -------- |
| Generic sort   |  O(n^2)  |
| Insertion sort |  O(n^2)  |
| Selection sort |  O(n^2)  |
| Merge sort     | Θ(nlogn) |
| Quick sort ran | Θ(nlogn) |
| Quick sort det: 1st/last element |  Θ(n^2)  |
| Quick sort det: pick median |  Θ(nlogn)  |
| Heap sort      | O(nlogn) |
| Couting sort   | O(n+k)   |
| Radix sort     | O(d(n+b))|


- `O(n^2)`: generic sort, insertion sort, quick sort deter
- `O(nlogn)`: Merge sort, Heap sort,  quick sort randomized
- `O(n)`: Radix sort, counting sort

### Quicksort ⚡️
[Questions to think through before quicksort](#pivot-i-and-j-positioning)
 **To maintain consistency, we will pick the strategy:**
  1. Move the pivot always to the beginning of the segment
  2. Initialize `i` at `low`, `j` at `low + 1`
  3. At the end swap `arr[i]` with `arr[low]`/`arr[pivot]`.
  4. If `def quick_sort_ran(arr, low, high)` choose to include `high`, then we should:
      -  use `len(arr)-1` as input
      -  input `pivot - 1` and `high`(since `len(arr)-1` used)
      -  `While j <= high`, should include `j==high`

#### Quicksort Randomized
![QS Animation](https://fullyunderstood.com/wp-content/uploads/2019/09/quicksort.gif)
*GIF from fullyunderstood.com*

### Heap sort 🌳
[Some questions to be cleared before heap sort 👈🏼](#pq-tree-and-heap-relationship)
**Heap sort** is a comparison-based sorting algorithm that uses a binary heap. It works by **building a heap from the input data**, then repeatedly **removing/extracting** the largest/smallest element from the heap and restoring the heap property, until the heap is empty. This process sorts the data in ascending order when a max-heap is used (or descending order if a min-heap is used).

**Heapify**
Heapify is used when removing or inserting an element into a heap, ensuring that the heap **remains a complete binary tree** and maintains its **order properties**.

**Insertion:**
**Deletion:**


### Counting Sort 🔢
[CS Dojo's YT video on counting sort](https://www.youtube.com/watch?v=OKd534EWcdk)
Counting sort is stable sorting algorithm, which keeps the original order of the element when ties occur. And counting sort works best when range of the numbers in an array is small(e.g. only 0,1,3 in the array.) 
**The steps of counting sorts are:**
1. Finding the starting index of every number, and store them in an auxiliary array.
2. Calculate the prefix sum of the array
3. Shift to the right by one element
4. Fill the new array based on the value of our auxiliary array
   - Increase the element encountered each time, and the value of auxiliary array 
   means the index of where the number should be placed.

**Runtime analysis ⏱**
T(n) = O(n+k), n is the length of the original array(total number of elements), k is the number value range in the array( [smallest, greatest] ).

Space complexity: An array of length n, and another array of length k. Thus, O(n+k).

### Radix Sort 💯
[CS Dojo's YT video on radix sort](https://www.youtube.com/watch?v=XiuSW_mEn7g)
Radix sort is sorting every numbers in the array digit-by-digit. Bsed on [counting sort](#counting-sort), radix sort is also stable.

**Runtime analysis ⏱**
Let's say:
- `n`: the length of the array 
- `d`: max digit number we need to represent all the elements
- `b`: base range where we sort in each level, such as in the base of 10, the range is [0,9]. It is also the length of the auxiliary array.

So `d` will be how many rounds of sorting we need to perform. In every round, we will carry out a counting sort in `O(n+b)`. So the overall runtime of `O(d(n+b))`, which could possibly fast than merge sort or quick sort. Choosing `b` and `d` can be a trade-off between time and space.

排序类（Sort）：
    基础知识：快速排序（Quick Sort）， 归并排序（Merge Sort）的原理与代码实现。需要能讲明白代码中每一行的目的。快速排序时间复杂度平均状态下O（NlogN），空间复杂度O（1），归并排序最坏情况下时间复杂度O（NlogN），空间复杂度O（N）
    入门题目：
        Leetcode 148. Sort List
        Leetcode 56. Merge Intervals
        Leetcode 27. Remove elements
    进阶题目：
        Leetcode 179. Largest Number
       Leetcode 75. Sort Colors
       Leetcode 215. Kth Largest Element
       Leetcode 4. Median of Two Sorted Arrays
注意：后两题是与快速排序非常相似的快速选择（Quick Select）算法，面试中很常考