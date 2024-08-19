from typing import List

class ListNode:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

class LRUCahe:    
    def __init__(self, capacity: int) -> None:
        # We can only have capacity ListNodes
        self.capacity = capacity
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hashmap = {}

    def put(self, key: int, value: int) -> None:
        # add nodes to linked list
        # update the hashmap

    def get(self, key: int) -> int:
        # move the nodes to the front of linked list
        # return the hash value

    def add(self, key: int) -> None:
        # add to the first position in nodes
        
    def remove(self, key: int) -> None:
        # remove the last nodes
