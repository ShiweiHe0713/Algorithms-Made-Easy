
并查集（Union Find）：把两个或者多个集合合并为一个集合
    基础知识：如果数据不是实时变化，本类问题可以用BFS或者DFS的方式遍历，如果数据实时变化（data stream）则并查集每次的时间复杂度可以视为O（1）；需要牢记合并与查找两个操作的模板
    常见题目：
        Leetcode 721 Accounts Merge
        Leetcode 547 Number of Provinces
        Leetcode 737 Sentence Similarity II
        Leetcode 305 Number of Islands II
字典树（Trie）
    基础知识：（https://zh.wikipedia.org/wiki/Trie）；多数情况下可以通过用一个set来记录所有单词的prefix来替代，时间复杂度不变，但空间复杂度略高
    常见题目：
        Leetcode 208 Implement Trie (Prefix Tree)
        Leetcode 211 Design Add and Search Words Data Structure
        Leetcode 1268 Search Suggestions System
        Leetcode 212 Word Search II
单调栈与单调队列（Monotone Stack／Queue）
    基础知识：单调栈一般用于解决数组中找出每个数字的第一个大于／小于该数字的位置或者数字；单调队列只见过一道题需要使用；不论单调栈还是单调队列，单调的意思是保留在栈或者队列中的数字是单调递增或者单调递减的常见题目：
        Leetcode 85 Maximum Rectangle
        Leetcode 84 Largest Rectangle in Histogram
        Leetcode 907 Sum of Subarray Minimums (与84类似)
        Leetcode 739 Daily Temperatures
        Leetcode 901 Online Stock Span
        Leetcode 503 Next Greater Element II
        Leetcode 239 Sliding Window Maximum （唯一的单调队列题）
扫描线算法（Sweep Line）
    基础知识：一个很巧妙的解决时间安排冲突的算法，本身比较容易些也很容易理解
    常见题目：
        Leetcode 253 Meeting Room II（Meeting Room I也可以使用）
        Leetcode 218 The Skyline Problem
        Leetcode 759 Employee Free Time
TreeMap
    基础知识：基于红黑树（平衡二叉搜索树）的一种树状 hashmap，增删查改、找求大最小均为logN复杂度，Python当中可以使用SortedDict替代；SortedDict继承了普通的dict全部的方法，除此之外还可以peekitem(k)来找key里面第k大的元素，popitem(k)来删除掉第k大的元素，弥补了Python自带的heapq没法logN时间复杂度内删除某个元素的缺陷；最近又在刷一些hard题目时候突然发现TreeMap简直是个神技，很多用别的数据结构写起来非常麻烦的题目，TreeMap解决起来易如反掌。
   常见题目：
        Leetcode 729 My Calendar I
        Leetcode 981 Time Based Key-Value Store
        Leetcode 846 Hand of Straights
        Leetcode 218 The Skyline Problem
        Leetcode 480. Sliding Window Median (这个题用TreeMap超级方便)
        Leetcode 318 Count of Smaller Numbers After Self (这个题线段树、二分索引树、TreeMap都可以)
