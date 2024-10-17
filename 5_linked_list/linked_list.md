# Linked List

**Table of contents**



## Conclusion

**Linked list problems are frequently related to two pointers, stacks/recursion**. Like we can use stack or recursion to reverse a linked list, use two pointers to find the mid point of a linked list or detect cycle in the list.



## Problems

### Operation type
基础知识：链表如何实现，如何遍历链表。链表可以保证头部尾部插入删除操作都是O（1），查找任意元素位置O（N）基础题目：
#### 206.Reverse Linked List

We'll have to learn both iterative and recursion approach to solve this problem. Iterative's space complexity is O(1) while the recursive one is O(n).

```python
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if length is <= 1
        if not head or not head.next:
            return head

        # reverse all the nodes in the back
        tail = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return tail
```



#### 876.Middle of the Linked List

#### [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

1. We have to use a dummy to store the head(cur), then move the cur all the way to the end.
2. Len == 1 is a edge case we have to handle manually
3. After finish traversing one array/list, we have to append the unfinished portion to the cur



### OOD

注意：快慢指针和链表反转几乎是所有链表类问题的基础，尤其是反转链表，代码很短，建议直接背熟。
#### 146. LRU Cache
In [LRU Cache](./lru_cache.py), if we use an array/list to implement the queue, operations will cost O(n). This is because we will frequently be removing elements from arbitrary positions in the list, which costs O(n); **We need a way to implement this queue such that the operations will run in O(1).**

**And the convention for linked list are:**
Head: Least recently used item (to be evicted first).
Tail: Most recently used item (updated or added most recently).

**Some improvements from my approach**
1. The value in hashmap is a ListNode, not value integer
2. We add and remove by passing ListNode not integer
3. **Insert at tail and remove at the head(esp remember to insert at the tail not head!!)**
4. Use `del self.dict[node.key]` to remove from hashmap after removing one element from the linked list.


- Leetcode 160. Intersection of Two Linked Lists
- Leetcode 141. Linked List Cycle (Linked List Cycle II)
- Leetcode 92. Reverse Linked List II
- Leetcode 328. Odd Even Linked List

