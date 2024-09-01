from typing import List

def binary_search(arr: List[int], target: int) -> int:
    l, r = 0, len(arr) - 1
    
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    
    return r

arr = [1,3,14,25,26]
print(binary_search(arr, 26))