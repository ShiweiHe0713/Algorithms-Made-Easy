from typing import List

class ListNode:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:    
    def __init__(self, capacity: int) -> None:
        # We can only have capacity ListNodes
        self.capacity = capacity
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hashmap = {}
# put (1,1) -> {1,1}, head->1->tail; 
# put(2,2) -> {1:1, 2:2}, head->2->1->tail; 
# get(1), {1:1, 2:2}, head->1->2->tail; 
# put(3,3), head->1->3->tail, {1:1, 3:3}
    def put(self, key: int, value: int) -> None:
        if key not in self.hashmap:
            if self.capacity == 0:
                self.remove()
                target = self.tail.prev.key
                del self.hashmap[target]
            # capacity > 0
            else:
                self.capacity -= 1
            self.add(key)
        else:
            # update the order in linked list
            self.remove()
            self.add(key)
        self.hashmap[key] = value
        print(self.tail.prev.key)

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        # move the nodes to the front of linked list
        self.remove()
        self.add(key)
        # return the hash value
        return self.hashmap[key]

    def add(self, key: int) -> None:
        """Add to the front of the linked list"""
        node = ListNode(key)
        node.next = self.head.next
        self.head.next.prev = node
        node.prev = self.head
        self.head.next = node

    def remove(self) -> None:
        """Remove the last list node before tail"""
        # remove the last nodes
        if not self.tail or not self.tail.prev:
            return
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev

# ["LRUCache","put","put","get","put","get","put","get","get","get"]
# [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
s = LRUCache(2)
s.put(1,1)
s.put(2,2)
print("print", s.get(1))
s.put(3,3)
print("print", s.get(2))

