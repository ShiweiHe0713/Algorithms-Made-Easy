import heapq

def heapify(arr, n, i):
    largest = i # Initialize largest as root
    l = 2 * i + 1 
    r = 2 * i + 2  
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    # Since last parent will be at (n//2) we can start at that location.
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)
    # One by one extract elements
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i]) # swap
        heapify(arr, i, 0)

# Driver code to test above
# arr = [12, 11, 13, 5, 6, 7, ]
# heapSort(arr)
# n = len(arr)
# print('Sorted array is')
# for i in range(n):
#     print(arr[i])
# Initial min-heap
        

heap = [60,50,40,30,20,10]
heapq.heapify(heap)
print(heap)

heapq.heappush(heap, 15)
print("Heap after insertion:", heap)

heapq.heappop()
print("Heap after insertion:", heap)
# Inserte 15 into [10, 20, 40, 30, 50, 60]
# Binary tree representaion of heapify up
#        10
#      /    \
#    20      40
#   / \     /
# 30  50   60  

# Inserte 15 arbitrarily 
#        10
#      /    \
#    20      40
#   / \     /  \
# 30  50   60   15

# Compare 15 with its parent, swap if smaller
#        10
#      /    \
#    20      15
#   / \     /  \
# 30  50   60   40

# Thus, we get [10,20,15,30,50,60,40]

# Delete a node in heap (Trickier than insertion)

# E.g.: Delete 15 from [10,20,15,30,50,60,40]
# Find the index of the element you want to remove.
# Swap the element with the last element in the heap.
# Remove the last element (now the one you want to remove).
# Since the swap can violate the heap property, you'll need to restore it. 
# If the swapped element is greater than its parent, you need to heapify down. 
# If it's less, you might need to heapify up.

# Swap 15 with the last element (Heapify down)
#        10
#      /    \
#    20      40
#   / \     /  \
# 30  50   60   15

# Then remove the last element
#        10
#      /    \
#    20      40
#   / \     /  
# 30  50   60   

# Now we get: [10,20,40,30,50,60]