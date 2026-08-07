#FIXME: Problem: Top K Frequent Elements
#FIXME: Link: https://leetcode.com/problems/top-k-frequent-elements/
#FIXME: Given: An integer array `nums` and an integer `k`
#FIXME: Return: The `k` most frequent elements (any order)
#FIXME: Constraints:
#FIXME:   - 1 <= nums.length <= 10^5
#FIXME:   - -10^4 <= nums[i] <= 10^4
#FIXME:   - k is always valid (1 <= k <= number of unique elements)
#FIXME:
#FIXME: Real-world scenario: You run a music app. Given a list of all song plays,
#FIXME: find the top k most played songs. Brute = count each song, sort the list.
#FIXME: Optimal = use a min-heap of size k (only keep the top k at all times).
#FIXME:
#FIXME: Fun fact: This is how Spotify's "Top Songs" and YouTube's "Trending" work —
#FIXME: they don't sort ALL videos. They maintain a small heap of top k only. Much faster.

import heapq
from collections import Counter


class Solution:
    #NOTE: Brute Force — O(n + m log m) time, O(n) space
    #NOTE: (where n = array length, m = unique elements)
    #TODO: Step 1: Count frequency using HashMap → O(n)
    #TODO: Step 2: Sort by frequency (descending) → O(m log m)
    #TODO: Step 3: Take first k elements → O(k)
    #TODO: Sathwik wrote his own bubble sort for this (sort_by_freq) — works but O(m²).
    #TODO: Using Python's built-in sort with lambda is cleaner and O(m log m).
    def brute(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1  #NOTE: The counting pattern (5th time using it!)
        items = list(freq.items())  #NOTE: Convert to list of (num, count) tuples
        items.sort(key=lambda x: x[1], reverse=True)  #NOTE: Sort by x[1] (count), highest first
        #NOTE: lambda x: x[1] means "for each tuple x, use index 1 (the count) as sort key"
        #NOTE: reverse=True means descending (highest frequency first)
        res = []
        for i in range(k):
            res.append(items[i][0])  #NOTE: items[i][0] = the number (not the count)
        return res

    #NOTE: Better — O(n) time, O(n) space (Using Counter.most_common)
    #TODO: Python's Counter does the counting AND has most_common(k) built in.
    #TODO: most_common(k) uses a heap internally — so it's O(n + k log m) but feels like O(n).
    #TODO: This is the INTERVIEW one-liner that shows you know Python.
    def better(self, nums: list[int], k: int) -> list[int]:
        return [x[0] for x in Counter(nums).most_common(k)]
        #NOTE: Counter(nums) → {1: 3, 2: 2, 3: 1}
        #NOTE: .most_common(2) → [(1, 3), (2, 2)]  (top 2 by frequency)
        #NOTE: [x[0] for x in ...] → [1, 2]  (extract just the numbers)

    #NOTE: Optimal — O(n + m log k) time, O(n) space (Min-Heap approach)
    #TODO: Key Insight: We don't need to sort ALL elements. Just maintain the TOP k.
    #TODO: Use a MIN-heap of size k. If heap grows beyond k, pop the smallest.
    #TODO: At the end, heap contains exactly the k most frequent elements.
    #TODO: Why min-heap? Because we want to REMOVE the least frequent — min is at top.
    #TODO: This is O(m log k) instead of O(m log m) — much better when k << m.
    def optimal(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        heap = []  #NOTE: Min-heap — smallest count at top
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))  #NOTE: Push (count, num) tuple
            if len(heap) > k:  #NOTE: If heap exceeds size k, remove smallest
                heapq.heappop(heap)  #NOTE: Pops the MINIMUM (least frequent) element
        return [num for count, num in heap]  #NOTE: Extract just the numbers from heap


#NOTE: ===== PYTHON TIPS & BUILT-INS =====
#NOTE:
#NOTE: LAMBDA FUNCTIONS:
#NOTE:   lambda x: x[1]  → anonymous function that returns x[1]
#NOTE:   Same as: def get_second(x): return x[1]
#NOTE:   Used in: .sort(key=lambda x: x[1])  → "sort by second element of each tuple"
#NOTE:   WHY lambda? Because .sort(key=...) needs a FUNCTION, not a value.
#NOTE:   You can't write .sort(key=x[1]) — x doesn't exist there. Lambda CREATES the function.
#NOTE:
#NOTE: .sort() FULL SYNTAX:
#NOTE:   list.sort(key=None, reverse=False)
#NOTE:   key = a function that extracts what to sort by (default: sort by element itself)
#NOTE:   reverse = True for descending, False for ascending (default)
#NOTE:   Examples:
#NOTE:     nums.sort()                                → ascending
#NOTE:     nums.sort(reverse=True)                    → descending
#NOTE:     tuples.sort(key=lambda x: x[1])            → sort by second element
#NOTE:     tuples.sort(key=lambda x: x[1], reverse=True)  → descending by second element
#NOTE:
#NOTE: SORTING TUPLES:
#NOTE:   items = [(1, 3), (2, 2), (3, 1)]
#NOTE:   items.sort(key=lambda x: x[1])              → sort by count ascending
#NOTE:   items.sort(key=lambda x: x[1], reverse=True) → sort by count descending
#NOTE:
#NOTE: LIST COMPREHENSION (one-liner for loop):
#NOTE:   [x[0] for x in [(1,3), (2,2)]]  → [1, 2]
#NOTE:   Same as: res = []; for x in list: res.append(x[0])
#NOTE:
#NOTE: COUNTER (from collections):
#NOTE:   Counter([1,1,1,2,2,3]) → Counter({1: 3, 2: 2, 3: 1})
#NOTE:   Same as doing the freq.get(num, 0) + 1 loop manually.
#NOTE:   .most_common(k) → returns top k as [(element, count)] tuples, sorted.
#NOTE:
#NOTE: HEAPQ MODULE:
#NOTE:   Python's heapq is a MIN-heap (smallest at top)
#NOTE:   heapq.heappush(heap, item) → add item, maintain heap property
#NOTE:   heapq.heappop(heap) → remove and return SMALLEST item
#NOTE:   For TUPLES: heap compares by FIRST element of tuple.
#NOTE:     heappush(heap, (count, num)) → sorts by count (first element)
#NOTE:   For a MAX-heap, push negative values: heappush(heap, -val)
#NOTE:
#NOTE: freq.items() vs list(freq.items()):
#NOTE:   freq.items() → dict_items object (NOT a list, can't sort directly!)
#NOTE:   list(freq.items()) → actual list of tuples, NOW you can sort it.
#NOTE:
#NOTE: ===== SATHWIK'S MISTAKES (Aug 7) =====
#NOTE: 1. Called .sort() on dict_items directly → must wrap with list() first
#NOTE: 2. Wrote reverse=true (lowercase t) → Python needs reverse=True (capital T)
#NOTE: 3. Forgot self.method_name() when calling helper inside class
#NOTE: 4. Overwrote dict itself (dict = dict.get(...)) instead of dict[key] = value


if __name__ == "__main__":
    obj = Solution()

    # Case 1: Basic case
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print("Case 1:")
    print("  Brute:", obj.brute(nums, k))      # [1, 2]
    print("  Better:", obj.better(nums, k))    # [1, 2]
    print("  Optimal:", obj.optimal(nums, k))  # [1, 2]

    # Case 2: Single element
    nums = [1]
    k = 1
    print("\nCase 2:")
    print("  Brute:", obj.brute(nums, k))      # [1]
    print("  Better:", obj.better(nums, k))    # [1]
    print("  Optimal:", obj.optimal(nums, k))  # [1]

    # Case 3: All same frequency
    nums = [1, 2, 3]
    k = 2
    print("\nCase 3:")
    print("  Brute:", obj.brute(nums, k))      # any 2 of [1, 2, 3]
    print("  Better:", obj.better(nums, k))
    print("  Optimal:", obj.optimal(nums, k))

    # Case 4: Larger array
    nums = [4, 1, -1, 2, -1, 2, 3]
    k = 2
    print("\nCase 4:")
    print("  Brute:", obj.brute(nums, k))      # [-1, 2]
    print("  Better:", obj.better(nums, k))    # [-1, 2]
    print("  Optimal:", obj.optimal(nums, k))  # [-1, 2]

    # Case 5: k equals unique elements
    nums = [3, 3, 5, 5, 7, 7]
    k = 3
    print("\nCase 5:")
    print("  Brute:", obj.brute(nums, k))      # [3, 5, 7]
    print("  Better:", obj.better(nums, k))    # [3, 5, 7]
    print("  Optimal:", obj.optimal(nums, k))  # [3, 5, 7]
