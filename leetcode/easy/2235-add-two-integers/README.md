# Add Two Integers

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two integers `num1` and `num2`, return  *the  **sum**  of the two integers*.

 

 **Example 1:** 

```
Input: num1 = 12, num2 = 5
Output: 17
Explanation: num1 is 12, num2 is 5, and their sum is 12 + 5 = 17, so 17 is returned.

```

 **Example 2:** 

```
Input: num1 = -10, num2 = 4
Output: -6
Explanation: num1 + num2 = -6, so -6 is returned.

```

 

 **Constraints:** 

- -100 <= num1, num2 <= 100

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 12.1 MB (beats 99.31%)  
**Submitted:** 2026-07-20T06:21:57.378Z  

```py
class Solution(object):
    def sum(self, num1, num2):
        sum=num1+num2
        return sum
        
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        
```

---

[View on LeetCode](https://leetcode.com/problems/add-two-integers/)