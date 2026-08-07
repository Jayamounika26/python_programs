# Valid Palindrome II

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string `s`, return `true`  *if the* `s` *can be palindrome after deleting  **at most one**  character from it*.

 

 **Example 1:** 

```
Input: s = "aba"
Output: true

```

 **Example 2:** 

```
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

```

 **Example 3:** 

```
Input: s = "abc"
Output: false

```

 

 **Constraints:** 

- 1 <= s.length <= 105
- s consists of lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 64 ms (beats 22.20%)  
**Memory:** 19.4 MB (beats 96.51%)  
**Submitted:** 2026-08-07T08:57:41.993Z  

```py
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return (
                    isPalindrome(left + 1, right)
                    or
                    isPalindrome(left, right - 1)
                )
            left += 1
            right -= 1

        return True
```

---

[View on LeetCode](https://leetcode.com/problems/valid-palindrome-ii/)