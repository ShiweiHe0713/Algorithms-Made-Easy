# Stack

## Parentheses

**In [1249. Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/),** the couple places that confused me was:

1. How to enter the stack, what is the while condition?
2. How to track the invalid brace index?
3. How to build the string given the invalid brace indices?

My original thoughts was put the string whole into the stack, then pop from it one by one. The problem of doing this that it doesn't capture the invalid right brace imediately, since it's popped already. **What we want is to find and remove valid pairs,** and spot a invalid right brace in that moment. 

关于括号类的，第一个if是check是否是左括号，是则push; 第二个是elif not stack，即不为左括号且栈为空的情况，return false或者其他如记录不合法当前不合法右括号的index；第三个else是合法右括号，则pop from the stack.



    Queue题目：
        Leetcode 225. Implement Stack using Queues
        Leetcode 346. Moving Average from Data Stream
        Leetcode 281. Zigzag Iterator
        Leetcode 1429. First Unique Number
        Leetcode 54. Spiral Matrix
        Leetcode 362. Design Hit Counter
   Stack题目：
        Leetcode 155. Min Stack (follow up
        Leetcode 716 Max Stack)
        Leetcode 232. Implement Queue using Stacks
        Leetcode 150. Evaluate Reverse Polish Notation
        Leetcode 224. Basic Calculator II (I, II, III, IV)
        **Leetcode 20. Valid Parentheses**
        Leetcode 1472. Design Browser History
        Leetcode 1209. Remove All Adjacent Duplicates in String II
        Leetcode 1249. Minimum Remove to Make Valid Parentheses
        **Leetcode 735. Asteroid Collision**