#FIXME: Problem: Contains Duplicate
#FIXME: Link: https://leetcode.com/problems/contains-duplicate/
#FIXME: Given: An integer array `nums`
#FIXME: Return: True if any value appears at least twice, False if every element is distinct
#FIXME: Constraints:
#FIXME:   - 1 <= nums.length <= 10^5
#FIXME:   - -10^9 <= nums[i] <= 10^9


class Solution:
    #NOTE: Brute Force — O(n²) time, O(1) space
    #TODO: Compare every element with every other element. If any match → duplicate found.
    #TODO: Like checking every student's ID card against every other student in a class.
    def brute(self, nums: list[int]) -> bool:
        if len(nums) <= 1:
            return False
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

    #NOTE: Optimal — O(n) time, O(n) space (HashSet approach)
    #TODO: Key Insight: A SET only stores UNIQUE values. If we try to add something
    #TODO: that's already in the set → duplicate found!
    #TODO: Think of it like a bouncer at a club with a guest list:
    #TODO:   - Each person walks in, bouncer checks the list
    #TODO:   - If name already on list → "You're already inside!" (duplicate)
    #TODO:   - If not → add name to list, let them in
    def optimal(self, nums: list[int]) -> bool:
        seen = set()  #NOTE: set() uses hash table internally — O(1) lookup, just like dict but keys-only
        for i in range(len(nums)):
            if nums[i] in seen:  #NOTE: `in` on set is O(1) average — same hash magic as dict
                return True
            seen.add(nums[i])  #NOTE: .add() inserts element into set. Duplicates auto-ignored by sets.
        return False


#NOTE: ===== PYTHON TIPS & BUILT-INS =====
#NOTE: set() → unordered collection of UNIQUE elements. O(1) add/lookup/delete.
#NOTE: set.add(x) → adds element. If already exists, does nothing (no error).
#NOTE: x in set → O(1) membership check. Same hash table as dict.
#NOTE: len(set(nums)) < len(nums) → one-liner to check duplicates! (but creates full set first)
#NOTE: ALTERNATIVE one-liner: return len(nums) != len(set(nums))
#TODO: The one-liner is clean but always creates the FULL set.
#TODO: Our loop approach can return early (as soon as first duplicate found) → faster in practice.


if __name__ == "__main__":
    obj = Solution()

    # Case 1: Empty array
    nums = []
    print("Case 1 (Empty):", obj.optimal(nums))  # False

    # Case 2: Single element
    nums = [5]
    print("Case 2 (Single):", obj.optimal(nums))  # False

    # Case 3: All unique
    nums = [1, 2, 3, 4, 5]
    print("Case 3 (Unique):", obj.optimal(nums))  # False

    # Case 4: Contains duplicates
    nums = [1, 2, 3, 1]
    print("Case 4 (Duplicate):", obj.optimal(nums))  # True

    # Case 5: All elements same
    nums = [7, 7, 7, 7]
    print("Case 5 (All same):", obj.optimal(nums))  # True

    # Case 6: Includes negatives
    nums = [-1, -2, -3, -1]
    print("Case 6 (Negatives):", obj.optimal(nums))  # True

    # Case 7: Large unique range
    nums = list(range(1000))
    print("Case 7 (Large unique):", obj.optimal(nums))  # False

    # Case 8: Large with duplicate at end
    nums = list(range(1000)) + [999]
    print("Case 8 (Large duplicate):", obj.optimal(nums))  # True
