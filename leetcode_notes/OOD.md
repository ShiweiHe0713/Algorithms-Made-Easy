# OOD

**The OOD problems are based on these principles:**

- **Reorder:** Move something from the middle of the DS to the end in `O(1)`, we should use **linked list**. Usually the operation `get()` or `visit()` is associated with this, because we want to move the node to one end of the DS.
- **Fast access:** Either use an array or hash map to achieve `O(1)` access.
- **Fast deletion:** 
  - O(1): Hashmap, hashset, linked list, array pop(), heap/pq top element
  - O(logn): 
  - O(n): array middle nodes

- **Subfunctions**

When design for the OOD problems, we will have some main functions, but we also need some subfunctions to seperate the functionalities. For example in LRU, we want to create 2 other functions `add` and `remove` to help achieve `put` and `get`.