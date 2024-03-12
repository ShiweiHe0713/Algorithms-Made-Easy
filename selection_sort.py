def selection_sort(arr):
    '''T(n) = Θ(n^2)'''
    n = len(arr)
    for i in range(n):
        min_ele_index = i
        for j in range(i, n):
            if(arr[j] <= arr[min_ele_index]):
                min_ele_index = j
        arr[i], arr[min_ele_index] = arr[min_ele_index], arr[i]

arr = [8,7,6,5,4,3,2,1]
selection_sort(arr)
print(arr)