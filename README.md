# Fundamental Algorithms
This is a repo that helps you to learn the **foundemental algorithms** as well as their **run time** analysis. The algorithms covered such as **divide and conquer**(binary search, fibonacci, etc), **sorting** algorithms(quick sort, heap sort, radix sort, etc), **BST**, **dynammic programming**, etc. 

Also to notice the material is partially based on *CSCI-GA-1170 Fundamental Algorithms* from 🎓 [NYU Courant](https://cims.nyu.edu/dynamic/). 

Enjoy your journey learning these fun algorithms! 🥳

**Table of content**
- [Fundamental Algorithms](#fundamental-algorithms)
  - [Divide and Conquer](#divide-and-conquer)
  - [Sorting](#sorting)
    - [Quicksort ⚡️](#quicksort-️)
      - [Quicksort Randomized](#quicksort-randomized)
    - [Heap sort 🌳](#heap-sort-)
    - [Counting Sort 🔢](#counting-sort-)
    - [Radix Sort 💯](#radix-sort-)
  - [Trees 🌲](#trees-)
    - [BST](#bst)
    - [2-3 Tree](#2-3-tree)
  - [Dynamic Programming](#dynamic-programming)
    - [Fibonacci sequence](#fibonacci-sequence)
    - [Cutting rod](#cutting-rod)
    - [Longest Common Subsequence](#longest-common-subsequence)
- [Appendix 🖇](#appendix-)
    - [PQ, Tree and heap relationship](#pq-tree-and-heap-relationship)
    - [Pivot, i, and j positioning](#pivot-i-and-j-positioning)
- [Reference 🗞](#reference-)

## Divide and Conquer
   pass

## Sorting
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

## Trees 🌲
### BST 
### 2-3 Tree

## Dynamic Programming 
Dynamic programming is wonderful way of solving recurrence in a faster way in trade-off of additional space complexity either by using tabulation or memoization. 
The primary purpose of using dynamic programming (DP) is to store and reuse the results of subproblems to avoid redundant calculations, thereby reducing the overall time complexity.
1. Brute force

2. Tabulation
  ```python
  def fibonacci_table(self) -> int:
          '''Tabulation (Bottom-Up) Approach'''
          n = self.n
          table = [None] * (n+1)
          table[0] = 0
          table[1] = 1
          for i in range(2, n+1):
              table[i] = table[i-1] + table[i-2]
          return table[n]
  ```
  In tabulation approach, recursion is not implemented, the value of table[n] is achieved using a loop to get a prefix sum from 2 to n. Since it is accumulated from 2 to 3 to 4 to n, it is a bottom-up approach.
  
3. Memoization

### Fibonacci sequence
**Definition: ** 
- fibonacci(0) = 0, fibonacci(1) = 1
- fibonacci(n) = fibonacci(n-1) + fibonacci(n-2), when n >= 2
[fibonacci.py](./4_dynammic_programming/fibonacci.py)

### Cutting rod

### Longest Common Subsequence


# Appendix 🖇
### PQ, Tree and heap relationship
We need to distinguish between `priority queue`, `heap`, `binary tree` and `array` before discussing the implementation of heap sort, because these concepts always intertwined and confused me while learning this sorting algorithm.
- `Priority queue`: A priority queue is an **abstract data type**(not a data structure) that operates similarly to a regular queue or stack but with a **"priority"** feature. A priority queue can be implemented using **various** data structures, including heaps (most commonly), binary trees, or even arrays.
- `Heap`: Heap is a **specialized** tree-based data structure where each node conform to the same rules(like max heap or min heap.) A Binray heap can also be implemented as an array for efficiency.
- `Binary tree`: A tree data structure in which each node has at most two children. It's a **fundamental** structure that can be specialized into more **specific types**, such as BST, AVL trees, and heaps.
- `Array`: Arrays can be used to implement binary heaps efficiently due to the **predictable structure of a complete binary tree**, where the relationships between parent and child nodes can be calculated using the indices.

**In conclusion**, a binary heap is a more specific type of binary tree, tailored for efficiently managing hierarchical data according to certain rules (heap property).
A priority queue is an abstract concept that specifies behavior (an ADT) rather than a concrete data structure. A binary heap is a specific data structure that efficiently implements the priority queue ADT.

### Pivot, i, and j positioning
1. Why do we need to put `arr[pivot]` somewhere "safe"? And where should we put it? First or last position?
2. Where should we initialize `i` and `j`?
3. In the last step of swapping `arr[pivot]` to the middle, which element should we switch with?
4. Where on earth does `arr[i]` point to?
   - The last element in "smaller" section? Or the first element in "greater" section? Or the first one of "uncompared" section?....
   - `i` points to the last index where an element is less than or equal to the pivot.
5. **"Two pointers"** algorithm in quick sort.
   - Quicksort also implemented **"Two pointers"** algorithm, where i is the slow pointer, and j is the fast pointer. `i` only moves if `arr[j]` is greater than `arr[pivot]`, and increments after swapping.


# Reference 🗞
1. [Visualgo](https://visualgo.net/en/sorting)
2. [Sort visualizer](https://sortvisualizer.com/)
3. [A greate article on QSR](https://www.baeldung.com/cs/randomized-quicksort)

[👆🏻 Go back to top 👆🏻](#fundamental-algorithms)