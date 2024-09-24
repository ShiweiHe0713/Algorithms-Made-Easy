class ListNode:
    def __init__(self, val: int, prev, next):
        self.prev = prev
        self.next = next
        self.val = val

class MyCircularQueue:

    def __init__(self, k: int):
        # queue = [None] * k
        self.capacity = k
        self.left = ListNode(-1, None, None)
        self.right = ListNode(-1, self.left, None)
        self.left.next = self.right

    def enQueue(self, value: int) -> bool:
        if self.capacity == 0:
            return False
        # append at the rear
        cur = ListNode(value, self.right.prev, self.right)
        self.right.prev = cur
        self.right.prev.prev.next = cur
        self.capacity -= 1
        return True
    
    def deQueue(self) -> bool:
        if self.left.next == self.right:
            return False
        self.left.next.next.prev = self.left
        self.left.next = self.left.next.next
        self.capacity += 1
        return True
    
    def Front(self) -> int:
        return self.left.next

    def Rear(self) -> int:
        return self.right.prev

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.capacity == 0


# Your MyCircularQueue object will be instantiated and called as such:
k = 3
obj = MyCircularQueue(k)
for i in range(5):
    obj.enQueue(i)
    
obj.isFull()

param_2 = obj.deQueue()
param_3 = obj.Front()
param_4 = obj.Rear()
param_5 = obj.isEmpty()
