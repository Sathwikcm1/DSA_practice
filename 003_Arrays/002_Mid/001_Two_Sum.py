#FIXME: Problem: Two Sum
#FIXME: Link: https://leetcode.com/problems/two-sum/
#FIXME: Given: A list of integers `nums` and an integer `target`
#FIXME: Return: Indices of the two numbers that add up to the target
#FIXME: Constraints:
#FIXME:   - 2 <= nums.length <= 10^4
#FIXME:   - -10^9 <= nums[i] <= 10^9
#FIXME:   - Only ONE valid answer exists
#FIXME:   - Can't use the same element twice


class Solution:
    #NOTE: Brute Force — O(n²) time, O(1) space
    #TODO: Try every possible pair. For each element, check every OTHER element.
    #TODO: Like checking every locker in a room one by one against every other locker.
    def brute(self, nums: list[int], target: int) -> list[int]:
        if len(nums) <= 1:
            return []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  #NOTE: Start from i+1 to avoid using same element twice
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    #NOTE: Optimal — O(n) time, O(n) space (HashMap approach)
    #TODO: Key Insight: If target = a + b, then b = target - a.
    #TODO: So for each number, calculate its complement (target - num).
    #TODO: If complement already exists in our HashMap, we found the pair!
    #TODO: Think of it like a register at a party:
    #TODO:   - Each person walks in and says "I need someone who is X to complete me"
    #TODO:   - If that someone already signed the register, MATCH!
    #TODO:   - Otherwise, sign yourself in and wait.
    def optimal(self, nums: list[int], target: int) -> list[int]:
        seen = {}  #NOTE: HashMap stores {number: index} — O(1) lookup
        for i, num in enumerate(nums):  #NOTE: enumerate gives (index, value) — Pythonic way to loop with index
            complement = target - num
            if complement in seen:  #NOTE: `in` on a dict checks keys in O(1) avg time (hash table lookup)
                return [seen[complement], i]
            seen[num] = i  #NOTE: Store current number and its index for future lookups
        return []


#NOTE: ===== PYTHON TIPS & BUILT-INS USED =====
#NOTE: enumerate(iterable) → yields (index, value) pairs. ALWAYS use this instead of range(len()) when you need both index and value.
#NOTE: `in` operator on dict → checks if KEY exists in O(1) average. Under the hood it's a hash table lookup.
#NOTE: dict[key] = value → stores key-value pair. If key exists, overwrites.
#NOTE: dict.get(key, default) → safer way to access. Returns default if key missing (avoids KeyError).
#NOTE: Type hints (list[int], -> list[int]) → not enforced at runtime, but helps readability and IDE support.


if __name__ == "__main__":
    sol = Solution()

    # Case 1: Normal positive numbers
    nums = [2, 7, 11, 15]
    target = 9
    print("Case 1:", sol.optimal(nums, target))  # [0, 1] → 2 + 7 = 9

    # Case 2: Includes negatives
    nums = [-3, 4, 3, 90]
    target = 0
    print("Case 2:", sol.optimal(nums, target))  # [0, 2] → -3 + 3 = 0

    # Case 3: Duplicates
    nums = [3, 3]
    target = 6
    print("Case 3:", sol.optimal(nums, target))  # [0, 1] → 3 + 3 = 6

    # Case 4: Single element (no solution)
    nums = [5]
    target = 5
    print("Case 4:", sol.optimal(nums, target))  # [] → can't use same element twice

    # Case 5: No solution at all
    nums = [1, 2, 3]
    target = 10
    print("Case 5:", sol.optimal(nums, target))  # [] → no pair adds up to 10

    # Case 6: Brute force comparison
    nums = [2, 7, 11, 15]
    target = 9
    print("Case 6 (brute):", sol.brute(nums, target))  # [0, 1]
