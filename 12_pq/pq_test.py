import heapq

min_heap = []
arr = [12,123,54,1,1231,3]
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 9)

heapq.heapify(arr)

print(arr)