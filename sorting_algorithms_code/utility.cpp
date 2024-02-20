#include "utility.hpp"

void Utility::printArray(int arr[], int n) {
    int n = sizeof(arr)/sizeof(arr[0]);
    for(int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void Utility::swap(int arr[], int i, int j) {
    int tmp = arr[j];
    arr[j] = arr[i];
    arr[i] = tmp;
}
