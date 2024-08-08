import random

def partition_ran(arr, low, high):
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
        pivot = partition_ran(arr, low, high)
        quick_sort_ran(arr, low, pivot - 1)
        quick_sort_ran(arr, pivot + 1, high)

def partition_determ(arr, low, high):
    pivot = high
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

def quick_sort_determ(arr, low, high):
    if low < high:
        pivot = partition_ran(arr, low, high)
        quick_sort_ran(arr, low, pivot - 1)
        quick_sort_ran(arr, pivot + 1, high)

