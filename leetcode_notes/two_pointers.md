# Two Pointers     
双指针（2 Pointer）：
    基础知识：常见双指针算法分为三类，同向（即两个指针都相同一个方向移动），背向（两个指针从相同或者相邻的位置出发，背向移动直到其中一根指针到达边界为止），相向（两个指针从两边出发一起向中间移动直到两个指针相遇）
   背向双指针：(基本上全是回文串的题)
        Leetcode 409. Longest Palindrome
        Leetcode 125. Valid Palindrome
        Leetcode 5. Longest Palindromic Substring
   相向双指针：(以two sum为基础的一系列题)

        Leetcode 1. Two Sum (这里使用的是先排序的双指针算法，不同于hashmap做法)
        Leetcode 167. Two Sum II - Input array is sorted
        Leetcode 15. 3Sum
        Leetcode 16. 3Sum Closest
        Leetcode 18. 4Sum
        Leetcode 454. 4Sum II
        Leetcode 277. Find the Celebrity
        Leetcode 11. Container With Most Water
    同向双指针：
        Leetcode 283. Move Zeroes
        Leetcode 26. Remove Duplicate Numbers in Array
        Leetcode 395. Longest Substring with At Least K Repeating Characters
        Leetcode 340. Longest Substring with At Most K Distinct Characters
        Leetcode 424. Longest Repeating Character Replacement
        Leetcode 76. Minimum Window Substring
        Leetcode 3. Longest Substring Without Repeating Characters
        Leetcode 1004 Max Consecutive Ones III

In [1570 Dot product of two sparse vectors](./1570_dot_product_of_two_sparse_vectors.py), we have to pay attention to:
1. Create instance attribute instead of class attribute, otherwise the data will be shared among instances.
2. When maintaining the length of the hashmap, the largest key should be kept not the count of elements.
3. When traversing hashmaps, the index edge should be inclusive, since the index is the key in hashmap.

Instead of using two pointers, we can also traverse one dict's items, and find if the index exist in another dict, saving more code.
