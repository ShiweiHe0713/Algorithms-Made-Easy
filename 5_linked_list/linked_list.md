# Linked List

**table of contents**
- [Linked List](#linked-list)
  - [题目](#题目)

In [LRU Cache](./lru_cache.py):
If we use an array/list to implement the queue, operations will cost O(n). This is because we will frequently be removing elements from arbitrary positions in the list, which costs O(n); **We need a way to implement this queue such that the operations will run in O(1).**

**And the convention for linked list are:**
Head: Least recently used item (to be evicted first).
Tail: Most recently used item (updated or added most recently).

**Some improvements from my approach**
1. The value in hashmap is a ListNode, not value integer
2. We add and remove by passing ListNode not integer
3. Insert at tail and remove at the head

## 题目
链表类（Linked List）：
    基础知识：链表如何实现，如何遍历链表。链表可以保证头部尾部插入删除操作都是O（1），查找任意元素位置O（N）基础题目：
        Leetcode 206. Reverse Linked List
        Leetcode 876. Middle of the Linked List
注意：快慢指针和链表反转几乎是所有链表类问题的基础，尤其是反转链表，代码很短，建议直接背熟。
    进阶题目:
        Leetcode 160. Intersection of Two Linked Lists
        Leetcode 141. Linked List Cycle (Linked List Cycle II)
        Leetcode 92. Reverse Linked List II
        Leetcode 328. Odd Even Linked List

