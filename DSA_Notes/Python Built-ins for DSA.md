# Python Built-in Functions & Methods — DSA Reference

> These are the functions/methods you'll use repeatedly in DSA and interviews.
> Organized by data structure. Learn these and you'll never be stuck on syntax again.

---

## How Many Are There?

Python has **71 built-in functions** total, but for DSA you only need about **25-30**.
Below are the ones that matter, grouped by what you'll use them on.

---

## 1. Numbers & Math

| Function | What it does | Example |
|----------|-------------|---------|
| `abs(x)` | Absolute value | `abs(-5)` → `5` |
| `max(a, b)` | Larger of two | `max(3, 7)` → `7` |
| `min(a, b)` | Smaller of two | `min(3, 7)` → `3` |
| `max(list)` | Largest in list | `max([1,5,3])` → `5` |
| `min(list)` | Smallest in list | `min([1,5,3])` → `1` |
| `sum(list)` | Sum of all | `sum([1,2,3])` → `6` |
| `pow(x, n)` | x to the power n | `pow(2, 3)` → `8` |
| `divmod(a, b)` | Quotient and remainder | `divmod(7, 2)` → `(3, 1)` |
| `round(x, n)` | Round to n decimals | `round(3.14159, 2)` → `3.14` |

### Integer Division & Modulo
```python
7 // 2   # → 3 (integer division, floor)
7 / 2    # → 3.5 (float division)
7 % 2    # → 1 (remainder/modulo)
```

---

## 2. Lists

### Creating
```python
nums = [1, 2, 3, 4, 5]
empty = []
zeros = [0] * 10          # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
range_list = list(range(5))  # [0, 1, 2, 3, 4]
```

### Methods

| Method | What | Example | Returns |
|--------|------|---------|---------|
| `.append(x)` | Add to end | `[1,2].append(3)` | `[1,2,3]` |
| `.pop()` | Remove & return last | `[1,2,3].pop()` | `3`, list is `[1,2]` |
| `.pop(i)` | Remove at index i | `[1,2,3].pop(0)` | `1`, list is `[2,3]` |
| `.insert(i, x)` | Insert at index | `[1,3].insert(1, 2)` | `[1,2,3]` |
| `.remove(x)` | Remove first occurrence | `[1,2,2,3].remove(2)` | `[1,2,3]` |
| `.sort()` | Sort in place | `[3,1,2].sort()` | `[1,2,3]` |
| `.sort(reverse=True)` | Sort descending | `[3,1,2].sort(reverse=True)` | `[3,2,1]` |
| `.sort(key=func)` | Sort by custom rule | see below | |
| `.reverse()` | Reverse in place | `[1,2,3].reverse()` | `[3,2,1]` |
| `.index(x)` | Find index of x | `[10,20,30].index(20)` | `1` |
| `.count(x)` | Count occurrences | `[1,1,2].count(1)` | `2` |
| `.extend(list2)` | Add all from list2 | `[1,2].extend([3,4])` | `[1,2,3,4]` |
| `.copy()` | Shallow copy | `b = a.copy()` | new list |

### Built-in Functions on Lists

| Function | What | Example |
|----------|------|---------|
| `len(list)` | Length | `len([1,2,3])` → `3` |
| `sorted(list)` | Returns NEW sorted list | `sorted([3,1,2])` → `[1,2,3]` |
| `reversed(list)` | Returns reversed iterator | `list(reversed([1,2,3]))` → `[3,2,1]` |
| `enumerate(list)` | (index, value) pairs | `list(enumerate(['a','b']))` → `[(0,'a'),(1,'b')]` |
| `zip(a, b)` | Pair elements | `list(zip([1,2],[3,4]))` → `[(1,3),(2,4)]` |

### .sort() vs sorted()
```python
nums = [3, 1, 2]

nums.sort()      # Modifies nums IN PLACE. Returns None.
sorted(nums)     # Returns a NEW sorted list. Original unchanged.
```

### Sorting with key (lambda)
```python
# .sort(key=function, reverse=bool)
# key = WHAT to sort by. Must be a function.
# reverse = True for descending

words = ["banana", "apple", "hi"]
words.sort(key=lambda x: len(x))  # sort by length → ["hi", "apple", "banana"]

tuples = [(1, 3), (2, 1), (3, 2)]
tuples.sort(key=lambda x: x[1])   # sort by second element → [(2,1), (3,2), (1,3)]
tuples.sort(key=lambda x: x[1], reverse=True)  # descending by second element
```

### Slicing
```python
nums = [0, 1, 2, 3, 4, 5]
nums[2:]     # [2, 3, 4, 5]   — from index 2 to end
nums[:3]     # [0, 1, 2]      — first 3 elements
nums[1:4]    # [1, 2, 3]      — index 1 to 3
nums[-2:]    # [4, 5]         — last 2 elements
nums[::-1]   # [5, 4, 3, 2, 1, 0] — reversed
```

---

## 3. Strings

| Method | What | Example |
|--------|------|---------|
| `.lower()` | Lowercase | `"Hello".lower()` → `"hello"` |
| `.upper()` | Uppercase | `"hello".upper()` → `"HELLO"` |
| `.strip()` | Remove whitespace | `" hi ".strip()` → `"hi"` |
| `.split(sep)` | Split into list | `"a,b,c".split(",")` → `["a","b","c"]` |
| `.join(list)` | Join list into string | `",".join(["a","b"])` → `"a,b"` |
| `.replace(old, new)` | Replace substring | `"hello".replace("l","x")` → `"hexxo"` |
| `.startswith(s)` | Check prefix | `"hello".startswith("he")` → `True` |
| `.endswith(s)` | Check suffix | `"hello".endswith("lo")` → `True` |
| `.isdigit()` | All digits? | `"123".isdigit()` → `True` |
| `.isalpha()` | All letters? | `"abc".isalpha()` → `True` |
| `.find(s)` | Find substring index | `"hello".find("ll")` → `2` |
| `len(s)` | Length | `len("hello")` → `5` |

### String tricks for DSA
```python
sorted("anagram")           # → ['a','a','a','g','m','n','r']
"".join(sorted("anagram"))  # → "aaagmnr" (sorted string)
ord('a')                    # → 97 (ASCII value)
chr(97)                     # → 'a' (character from ASCII)
```

---

## 4. Dictionaries (HashMap)

| Method | What | Example |
|--------|------|---------|
| `d.get(key, default)` | Safe access | `d.get("x", 0)` → `0` if "x" missing |
| `d.keys()` | All keys | `{"a":1}.keys()` → `dict_keys(["a"])` |
| `d.values()` | All values | `{"a":1}.values()` → `dict_values([1])` |
| `d.items()` | Key-value tuples | `{"a":1}.items()` → `[("a", 1)]` |
| `d.pop(key, default)` | Remove & return | `d.pop("a", None)` |
| `d.setdefault(key, val)` | Set if missing | `d.setdefault("x", [])` |
| `d.update(d2)` | Merge another dict | `d.update({"b": 2})` |
| `key in d` | Check if key exists | `"a" in d` → `True/False` (O(1)!) |

### The Counting Pattern (you know this!)
```python
freq = {}
for num in nums:
    freq[num] = freq.get(num, 0) + 1
```

### Converting dict to sortable list
```python
freq = {1: 3, 2: 2, 3: 1}
items = list(freq.items())  # [(1, 3), (2, 2), (3, 1)] — NOW you can sort
# CANNOT sort freq.items() directly — must wrap in list() first!
```

---

## 5. Sets (HashSet)

| Method/Op | What | Example |
|-----------|------|---------|
| `s.add(x)` | Add element | `{1,2}.add(3)` → `{1,2,3}` |
| `s.remove(x)` | Remove (error if missing) | `{1,2}.remove(1)` → `{2}` |
| `s.discard(x)` | Remove (no error) | `{1,2}.discard(5)` → `{1,2}` |
| `x in s` | Check membership | `3 in {1,2,3}` → `True` (O(1)!) |
| `a & b` | Intersection | `{1,2,3} & {2,3,4}` → `{2,3}` |
| `a \| b` | Union | `{1,2} \| {3,4}` → `{1,2,3,4}` |
| `a - b` | Difference | `{1,2,3} - {2}` → `{1,3}` |
| `len(s)` | Size | `len({1,2,3})` → `3` |

---

## 6. Collections Module (import needed)

```python
from collections import Counter, defaultdict, deque
```

| Class | What | When to use |
|-------|------|-------------|
| `Counter(list)` | Frequency dict | Counting problems (Majority Element, Top K) |
| `defaultdict(type)` | Dict with default values | Grouping (Group Anagrams) |
| `deque()` | Double-ended queue | BFS, sliding window |

```python
# Counter
Counter([1,1,2,3,3,3])         # → {3: 3, 1: 2, 2: 1}
Counter("anagram")              # → {'a': 3, 'n': 1, ...}
Counter(nums).most_common(k)    # → top k as [(elem, count)]

# defaultdict
d = defaultdict(list)
d["fruits"].append("apple")     # No KeyError! Auto-creates empty list.

# deque
q = deque()
q.append(1)       # add to right
q.appendleft(2)   # add to left
q.pop()           # remove from right
q.popleft()       # remove from left — O(1)! (list.pop(0) is O(n))
```

---

## 7. Heapq Module (import needed)

```python
import heapq
```

| Function | What |
|----------|------|
| `heapq.heappush(heap, item)` | Push item, maintain min-heap |
| `heapq.heappop(heap)` | Pop smallest item |
| `heap[0]` | Peek at smallest (don't remove) |
| `heapq.heapify(list)` | Convert list to heap in-place O(n) |

```python
# Min-heap (smallest at top):
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)
heap[0]           # → 2 (smallest)
heapq.heappop(heap)  # → 2 (removes smallest)

# Tuples: heap sorts by FIRST element
heapq.heappush(heap, (3, "apple"))
heapq.heappush(heap, (1, "banana"))
heapq.heappop(heap)  # → (1, "banana") — smallest first element

# Max-heap trick: push negatives
heapq.heappush(heap, -5)  # now -5 is "smallest"
```

---

## 8. Essential Built-in Functions

| Function | What | DSA Use |
|----------|------|---------|
| `len(x)` | Length of anything | Everywhere |
| `range(n)` | Numbers 0 to n-1 | Loops |
| `range(a, b)` | Numbers a to b-1 | Loops |
| `enumerate(list)` | (index, value) pairs | When you need both index AND value |
| `zip(a, b)` | Pair up two lists | Parallel iteration |
| `map(func, list)` | Apply func to each | `list(map(int, ["1","2"]))` → `[1,2]` |
| `filter(func, list)` | Keep items where func is True | `list(filter(lambda x: x>2, [1,2,3,4]))` → `[3,4]` |
| `any(list)` | True if ANY element is truthy | `any([0, 0, 1])` → `True` |
| `all(list)` | True if ALL elements are truthy | `all([1, 1, 0])` → `False` |
| `isinstance(x, type)` | Type check | `isinstance(5, int)` → `True` |
| `type(x)` | Get type | `type([])` → `<class 'list'>` |
| `int(x)` | Convert to int | `int("5")` → `5` |
| `str(x)` | Convert to string | `str(5)` → `"5"` |
| `list(x)` | Convert to list | `list("abc")` → `["a","b","c"]` |
| `set(x)` | Convert to set | `set([1,1,2])` → `{1,2}` |
| `dict(x)` | Convert to dict | `dict([("a",1)])` → `{"a": 1}` |
| `tuple(x)` | Convert to tuple | `tuple([1,2])` → `(1, 2)` |
| `bool(x)` | Convert to bool | `bool(0)` → `False`, `bool(1)` → `True` |

---

## 9. Lambda Functions

```python
# Syntax: lambda parameters: expression
# Same as a one-line function without a name

# Normal function:
def double(x):
    return x * 2

# Lambda equivalent:
double = lambda x: x * 2

# WHY? Used as throwaway functions in sort(), map(), filter()
# .sort(key=...) NEEDS a function. Lambda creates one inline.

# Examples:
lambda x: x[0]         # return first element of x
lambda x: x[1]         # return second element of x
lambda x: len(x)       # return length of x
lambda x: -x           # return negative (for max-heap trick)
lambda x, y: x + y     # two parameters
```

### WHY can't you write .sort(key=x[1])?
```python
items.sort(key=x[1])           # ❌ ERROR — x doesn't exist here
items.sort(key=lambda x: x[1]) # ✅ — creates a function that WILL receive x
```
`.sort()` calls your function internally: `for each item: sort_value = your_func(item)`. You must give it something callable.

---

## Learning Order (Recommended)

1. ✅ **Lists** — you use these every problem
2. ✅ **Dict** — HashMap counting pattern
3. ✅ **Sets** — HashSet for existence checks
4. ✅ **Strings** — manipulation methods
5. ✅ **Sorting + Lambda** — you just learned this
6. ⬜ **Collections (Counter, defaultdict, deque)** — next few problems
7. ⬜ **Heapq** — Top K problems, priority queues
8. ⬜ **List comprehension** — one-liners (optional but clean)

You're at step 5-6 right now. Solid progress.
