// Sort an array in non-decreasing order using merger_sort
#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

void printArray(vector<int> vec) {
	for(int i = 0; i < vec.size(); i++) {
		printf("%d ", vec[i]);
	}
	printf("\n");
}

void swap(vector<int>& vec, int i, int j) {
	int tmp = vec[j];
	vec[j] = vec[i];
	vec[i] = tmp;
}


void mergeSort(vector<int>& arr, int l, int r) {
	// divide & conquer
	int m = arr.size() / 2;
	// vector<int> left(arr.begin(), arr.begin() + m);
	// vector<int> right(arr.begin() + m + 1, arr.begin() + arr.size());
	mergeSort(arr, l, m);
	mergeSort(arr, m + 1, r);

	vector<int> result;
	
	while(left.size() != 0 && right.size() != 0) {
		if(left[0] <= right[0]) {
			result.push_back(left[0]);
			left.erase(left.begin());
		} else {
			result.push_back(right[0]);
			right.erase(right.begin());
		}
	}

	while(left.size() != 0) {
		result.push_back(left[0]);
		left.erase(left.begin());
	}

	while(right.size() != 0) {
		result.push_back(right[0]);
		right.erase(right.begin());
	}
}

int main() {
	vector<int> vec{3,1,2,5,4};

}