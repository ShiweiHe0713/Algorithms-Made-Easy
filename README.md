# Sorting algorithms visualizer
This is a website visualizer for different sorting algorithms: (Insertion Sort)IS, (Merge Sort)MS, (Quick Sort)QS, (Heap Sort)HS, etc.

*Sorting*
| Sorting        |   Time   |
| ------------   | -------- |
| Generic sort   |  O(n^2)  |
| Insertion sort |  O(n^2)  |
| Selection sort |  O(n^2)  |
| Merge sort     | Θ(nlogn) |
| Quick sort ran | Θ(nlogn) |
| Quick sort det: 1st/last element |  Θ(n^2)  |
| Quick sort det<br> pick median |  Θ(n^2)  |
| Heap sort      | O(nlogn) |
| Radix sort     | O() |
| Couting sort   | O() |


- `O(n^2)`: generic sort, insertion sort, quick sort deter
- `O(nlogn)`: Merge sort, Heap sort,  quick sort randomized
- `O(n)`: Radix sort, counting sort

# Quicksort
## Some question must be cleared 🤯
1. Why do we need to put `arr[pivot]` somewhere "safe"? And where should we put it? First or last position?
2. Where should we initialize `i` and `j`?
3. In the last step of swapping `arr[pivot]` to the middle, which element should we switch with?
4. Where on earth does `arr[i]` point to?
   - The last element in "smaller" section? Or the first element in "greater" section? Or the first one of "uncompared" section?....
   - `i` points to the last index where an element is less than or equal to the pivot.
5. **"Two pointers"** algorithm in quick sort.
   - Quicksort also implemented **"Two pointers"** algorithm, where i is the slow pointer, and j is the fast pointer. `i` only moves if `arr[j]` is greater than `arr[pivot]`, and increments after swapping.

 **To maintain consistency, we will pick the strategy:**
  1. Move the pivot always to the beginning of the segment
  2. Initialize `i` at `low`, `j` at `low + 1`
  3. At the end swap `arr[i]` with `arr[low]`/`arr[pivot]`.
  4. If `def quick_sort_ran(arr, low, high)` choose to include `high`, then we should:
      -  use `len(arr)-1` as input
      -  input `pivot - 1` and `high`(since `len(arr)-1` used)
      -  `While j <= high`, should include `j==high`

## Quicksort Randomized
![QS Animation](https://fullyunderstood.com/wp-content/uploads/2019/09/quicksort.gif)
*GIF from fullyunderstood.com*


# Reference
1. [Visualgo](https://visualgo.net/en/sorting)
2. [Sort visualizer](https://sortvisualizer.com/)
3. [A greate article on QSR](https://www.baeldung.com/cs/randomized-quicksort)