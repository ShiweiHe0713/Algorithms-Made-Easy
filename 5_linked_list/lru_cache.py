class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:    
    def __init__(self, capacity: int) -> None:
        # We can only have capacity ListNodes
        self.capacity = capacity
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dict = {}

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        # If exist, return the value
        node = self.dict[key]

        # Move the node to the end
        self.remove(node)
        self.insert(node)
        return node.value
    
    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            self.remove(node)
        node = ListNode(key, value)
        self.dict[key] = node
        self.insert(node)
        
        # if exceed capacity, remove the oldest
        if (len(self.dict) > self.capacity):
            old_node = self.head.next
            self.remove(old_node)
            # delete the hashmap entry
            del self.dict[old_node.key]

    def insert(self, node: ListNode) -> None:
        """insert at the tail of the linked list"""
        tmp = self.tail.prev
        tmp.next = node
        node.prev = tmp
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node: ListNode) -> None:
        """Remove the LRU node, by the head"""
        node.next.prev = node.prev
        node.prev.next = node.next
