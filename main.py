from quick_sort import *
from generic_sort import *

def main():
    arr = [8,7,6,5,4,3,2,1]
    print("Unsorted Array")
    print(arr)

    # quick_sort_ran(arr, 0, len(arr)-1)
    quick_sort_determ(arr, 0, len(arr)-1)

    print('Sorted Array in Ascending Order:')
    print(arr)

if __name__ == "__main__":
    main()
