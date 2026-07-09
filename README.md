# 🧠 Daily DSA questions

---

## 🔥 Current Streak

**X days**

---

## ✅ Progress Tracker

| Topic | Total | Done | Status |
|---|---|---|---|
| Arrays & Hashing | 9 | 0 | 🔴 Not started |
| Two Pointers | 5 | 0 | 🔴 Not started |
| Sliding Window | 6 | 0 | 🔴 Not started |
| Stack | 7 | 0 | 🔴 Not started |
| Binary Search | 7 | 0 | 🔴 Not started |
| Linked List | 11 | 0 | 🔴 Not started |
| Trees | 15 | 0 | 🔴 Not started |
| Tries | 3 | 0 | 🔴 Not started |
| Heap / Priority Queue | 7 | 0 | 🔴 Not started |
| Intervals | 6 | 0 | 🔴 Not started |
| Greedy | 8 | 0 | 🔴 Not started |
| Advanced Graphs | 6 | 0 | 🔴 Not started |
| Graphs | 9 | 0 | 🔴 Not started |
| Dynamic Programming 1D | 12 | 0 | 🔴 Not started |
| Dynamic Programming 2D | 11 | 0 | 🔴 Not started |
| Bit Manipulation | 7 | 0 | 🔴 Not started |
| Math & Geometry | 8 | 0 | 🔴 Not started |
| **Total** | **150** | **0** | |

> Update the **Done** column and status emoji as you complete each topic:
> 🔴 Not started · 🟡 In progress · 🟢 Complete

---

## 📝 Solution Template

Every file follows this structure:

```python
"""
Problem : Contains Duplicate (LC-217)
Link    : https://leetcode.com/problems/contains-duplicate/
Difficulty: Easy
Topic   : Arrays & Hashing

Approach:
  Use a hash set. Iterate through nums — if the current element is
  already in the set, return True. Otherwise add it. Return False if
  no duplicate found.

Time Complexity : O(n)
Space Complexity: O(n)
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
```

## 📚 Resources

- [NeetCode Roadmap](https://neetcode.io/roadmap)
- [NeetCode YouTube](https://www.youtube.com/@NeetCode)
- [LeetCode](https://leetcode.com)
