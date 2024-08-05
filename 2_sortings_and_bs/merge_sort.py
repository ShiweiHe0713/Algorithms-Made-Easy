def merge(arr, l, m, r):
    l_len = m - l + 1
    r_len = r - m

    # Create L and R array
    L = arr[l:m+1]      #[l,m]
    R = arr[m+1:r+1]    #[m+1,r]
    i = j = 0
    k = l
    # Modify arr in-place
    while i < l_len and j < r_len:
        if(L[i] <= R[j]):
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < l_len:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < r_len:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, l, r):
    if(l < r):
        mid = l + (r - l) // 2
        merge_sort(arr, l, mid)
        merge_sort(arr, mid + 1, r)
        merge(arr, l, mid, r)

        