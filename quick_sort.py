import random

def partition(arr, low, high):
    pivot = random.randint(low, high)
    arr[low], arr[pivot] = arr[pivot], arr[low]
    pivot = low
    i = low
    j = low + 1

    while j <= high: # include the last element
        if arr[j] <= arr[pivot]:
            i += 1 # increment before or after swapping?
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    arr[i], arr[pivot] = arr[pivot], arr[i]
    return i

def quick_sort_ran(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort_ran(arr, low, pivot - 1)
        quick_sort_ran(arr, pivot + 1, high)

arr = [8,7,6,5,4,3,2,1]
quick_sort_ran(arr, 0, len(arr)-1)
print(arr)
