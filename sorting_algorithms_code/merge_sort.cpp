// Sort an array in non-decreasing order using merger_sort
#include <iostream>
#include <cstdio>

void merge(int arr[], int left, int mid, int right) {
    // The length of left and right segment
    int l = mid - left + 1;
    int r = right - mid;

    // Create two array for left and right
    int L[l], R[r];
    
    // Fill the L and R
    for(int i = 0; i < l; i++) {
        L[i] = arr[left + i];
    }
    for(int i = 0; i < r; i++) {
        R[i] = arr[mid + i + 1];
    }

    // Merge to the master array
    int i = 0, j = 0, k = left;
    while(i < l && j < r) {
        if(L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
    
    // If L or R is not exhaugsted
    while(i < l) {arr[k++] = L[i++];}
    while(j < r) {arr[k++] = R[j++];}
}

void mergeSort(int arr[], int left, int right) {
    if(left >= right) return;
    int mid = left + (right - left)/2;
    mergeSort(arr, left, mid);
    mergeSort(arr, mid + 1, right);
    merge(arr, left, mid, right);
}

void printArr(int arr[], int size) {
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main() {
    int arr[] = {4,2,3,6,1,8,7};
    int left = 0, right = sizeof(arr)/sizeof(arr[0]) - 1;
    // mergeSort(arr, left, right);
    
    printArr(arr, right + 1);
}