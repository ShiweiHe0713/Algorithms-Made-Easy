// Sort an array in non-decreasing order using generic sort
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

void genericSort(vector<int>& vec) {
	// Time complexity: O(n^2)
	for(int i = 0; i < vec.size(); i++) {
		for(int j = i; j < vec.size(); j++) {
			if(vec[j] < vec[i]) {
				swap(vec, i, j);
			}
		}
	}
}

int main() {
	vector<int> vec{3,1,2,5,4};
	genericSort(vec);
	printArray(vec);
}
