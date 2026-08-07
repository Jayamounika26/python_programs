# Majority Element II

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array of size `n`, find all elements that appear more than `⌊n / 3⌋` times.

 

 **Example 1:** 

```
Input: nums = [3,2,3]
Output: [3]

```

 **Example 2:** 

```
Input: nums = [1]
Output: [1]

```

 **Example 3:** 

```
Input: nums = [1,2]
Output: [1,2]

```

 

 **Constraints:** 

- 1 <= nums.length <= 5 * 104
- -109 <= nums[i] <= 109

 

 **Follow up:**  Could you solve the problem in linear time and in `O(1)` space?

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 92.64%)  
**Memory:** 22.6 MB (beats 53.89%)  
**Submitted:** 2026-08-07T08:52:36.540Z  

```py
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1 = None
        candidate2 = None

        count1 = 0
        count2 = 0

        # First pass: find possible candidates
        for num in nums:

            if candidate1 == num:
                count1 += 1

            elif candidate2 == num:
                count2 += 1

            elif count1 == 0:
                candidate1 = num
                count1 = 1

            elif count2 == 0:
                candidate2 = num
                count2 = 1

            else:
                count1 -= 1
                count2 -= 1

        # Second pass: verify
        ans = []

        if nums.count(candidate1) > len(nums) // 3:
            ans.append(candidate1)

        if candidate2 != candidate1 and nums.count(candidate2) > len(nums) // 3:
            ans.append(candidate2)

        return ans
```

---

[View on LeetCode](https://leetcode.com/problems/majority-element-ii/)