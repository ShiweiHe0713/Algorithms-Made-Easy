# Mono stack

记住经常push到Mono stack里的是index而不是value，因为我们要定位这个元素并填充结果数组里相应的值，**所以在push的时候要想清楚到底是push值还是index**。



#### [1944. Number of Visible People in a Queue](https://leetcode.com/problems/number-of-visible-people-in-a-queue/)

After figuring out it's a mono stack problem, **the things that confused is me whether should I use an increasing or decreasing mono stack?**

To reframe this question is "**What order do we want to maintain?**", "**Are we looking for next larger or smaller element?**"

Then we see the question, we want to know all the taller person to its right, which means we look for all the larger element to one's right. 

拿Decreasing monostack 举例，当我们遍历数组的时候，我们遇到比top元素小的元素时，直接enqueue他们，遇到比top大的元素时，就要一直pop栈，直到cur_element < stack.top(). **所以我们用decreasing mono stack就是在寻找下个大于当前元素的第一个值**, 这两者之间的值都比他俩小。**我们永远都是对被pop掉的元素做些什么**，因为他们要不就是比新元素小或者大。



#### [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)

**Firstly,  why using an increasing mono stack instead of a decreading one?**

If we encounter a new element that's smaller than top element, we will keep popping until the top element is smaller or equal to the current element. Everytime we pop an element, we will take the [i - stack[-1] + 1] * 

- ocean view
- daily temperature
- number of visible people in a queue

