import random
from time_analysis import arithmetic_sequence_sum

def generic_sort(arr):
    '''Generic sort is the brute force sorting algorithm, with a run time of O(n^2)'''

    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if(arr[j] <= arr[i]):
                (arr[i], arr[j]) = (arr[j], arr[i])
    
    print(f"Number of comparisons: %d" %arithmetic_sequence_sum(len(arr)))
    print("Generic sort: Time complexity is O(n^2)")

def merge_sort(arr):
    pass
