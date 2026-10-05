# 008 — Linear Search

> **Pattern:** Linear Scan
> **Striver's Sheet:** Arrays Easy
> **Back to:** [[DSA Index]] → [[003_Arrays Easy]]

---

## Problem Statement

Search for a given element `k` in an array. Return its **index** if found, `-1` if not.

```
Input:  arr = [1, 2, 3, 4, 5], k = 3
Output: 2 (index of 3)
```

---

## Approaches

| Approach | Method | Time | Space |
|----------|--------|------|-------|
| **Pythonic** | `k in arr` — returns True/False | O(n) | O(1) |
| **Optimal (Interview)** | Explicit loop with `enumerate()`, returns index | O(n) | O(1) |

> There's no "better" here — linear search IS the only option for unsorted arrays. For sorted arrays, you'd use **Binary Search** (O(log n)).

---

## Code

```python
class Solution:
    def brute(self, arr: list[int], k: int) -> bool:
        return k in arr

    def optimal(self, arr: list[int], k: int) -> int:
        for i, num in enumerate(arr):
            if num == k:
                return i
        return -1
```

---

## Hardware Analogy

**Time O(n):** Imagine searching for a specific book on a shelf with no labels. You check each book one by one — if there are 1000 books, worst case you check all 1000. That's O(n). Your CPU does one comparison per element.

**Why O(1) space:** You're not creating any new data structures — just walking through with a pointer. No extra RAM allocated.

---

## Pythonic Tip: `enumerate()`

```python
# Instead of:
for i in range(len(arr)):
    if arr[i] == k:
        return i

# Use:
for i, num in enumerate(arr):
    if num == k:
        return i
```

`enumerate()` gives you `(index, value)` tuples — cleaner, no manual indexing.

---

## Real-Life Use Case

- **Ctrl+F in a text editor** — scans character by character (linear search on text)
- **Looking up a contact in an unsorted phone list** — check each entry
- **grep/rg in terminal** — linear scan through file contents

---

## Key Takeaway

> [!tip] When to use Linear Search vs Binary Search
> - **Unsorted data** → Linear Search O(n) is your ONLY option
> - **Sorted data** → Binary Search O(log n) is always better
> - Python's `in` operator on lists is O(n). On `set`/`dict` it's O(1) — because those use hash tables!
