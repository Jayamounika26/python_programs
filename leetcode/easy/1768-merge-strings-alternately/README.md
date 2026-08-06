# Merge Strings Alternately

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, starting with `word1`. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return  *the merged string.* 

 

 **Example 1:** 

```
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

```

 **Example 2:** 

```
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s

```

 **Example 3:** 

```
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d

```

 

 **Constraints:** 

- 1 <= word1.length, word2.length <= 100
- word1 and word2 consist of lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 36 ms (beats 95.03%)  
**Memory:** 19.3 MB (beats 17.84%)  
**Submitted:** 2026-08-06T05:59:48.836Z  

```py
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        ans = []
        while i < len(word1) and j < len(word2):
            ans.append(word1[i])
            ans.append(word2[j])
            i += 1
            j += 1
        while i < len(word1):
            ans.append(word1[i])
            i += 1
        while j < len(word2):
            ans.append(word2[j])
            j += 1
        return "".join(ans)     
```

---

[View on LeetCode](https://leetcode.com/problems/merge-strings-alternately/)