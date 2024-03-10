import random

def arithmetic_sequence_sum(n):
    sum = (1 + n) * n / 2
    return sum

def geometric_sequence_sum(n):
    pass

def factorial(n):
    if(n == 1):
        return 1
    return n * factorial(n-1)

def generic_sort(arr):
    '''Generic sort is the brute force sorting algorithm, with a run time of O(n^2)'''

    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if(arr[j] <= arr[i]):
                (arr[i], arr[j]) = (arr[j], arr[i])
    
    print(f"Number of comparisons: %d" %arithmetic_sequence_sum(len(arr)))
    print("Generic sort: Time complexity is O(n^2)")

def insertion_sort(arr):
    pass

def merge_sort(arr):
    pass

def partition(arr, low, high, fashion):
    '''
    Target of partitions is, given an array and an element 'x' of array as a pivot:
    1. Put x at its correct position in a sorted array (often forgotten)
    2. Put all smaller elements (smaller than x) before x
    3. Put all greater elements (greater than x) after x
    '''
    if fashion == "deterministic":
        pivot = arr[high]
    elif fashion == "randomized":
        # Todo: QS_ran not working correctly
        ran = random.randint(low, high)
        pivot = arr[ran]
    elif fashion == "median":
        mid = low + (high - low)/2
        pivot = arr[mid]

    i = j = low

    while(j<high):
        if(arr[j] <= pivot):
            (arr[j], arr[i]) = (arr[i], arr[j])
            i += 1
        j += 1
    (arr[i], arr[high]) = (arr[high], arr[i]) # i's successor must be greater than pivot
    return i

def quick_sort_deterministic(arr, low, high):
    if(low < high):
        pivot = partition(arr, low, high, "deterministic")
        quick_sort_deterministic(arr, low, pivot - 1)
        quick_sort_deterministic(arr, pivot + 1, high - 1)
    

def quick_sort_randomized(arr, low, high):
    '''
    Quick sort utilizes the idea of Divide and Conquer: Pivoting and Patitioning
    '''
    if(low < high):
        pivot = partition(arr, low, high, "randomized")
        quick_sort_randomized(arr, low, pivot - 1)
        quick_sort_randomized(arr, pivot + 1, high - 1)



def quick_sort_general(arr):

    pass


def main():
    arr = [8,7,6,5,4,3,2,1]
    print("Unsorted Array")
    print(arr)

    quick_sort_randomized(arr, 0, len(arr)-1)

    print('Sorted Array in Ascending Order:')
    print(arr)

if __name__ == "__main__":
    main()
