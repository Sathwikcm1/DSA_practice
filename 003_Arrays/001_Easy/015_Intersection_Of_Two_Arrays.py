#FIXME: Problem: Intersection of Two Arrays
#FIXME: Link: https://leetcode.com/problems/intersection-of-two-arrays/
#FIXME: Given: Two integer arrays `nums1` and `nums2`
#FIXME: Return: An array of their intersection (each element must be UNIQUE)
#FIXME: Constraints:
#FIXME:   - 1 <= nums1.length, nums2.length <= 1000
#FIXME:   - 0 <= nums1[i], nums2[i] <= 1000
#FIXME:
#FIXME: Real-world scenario: You have two guest lists for different events.
#FIXME: Find people who attended BOTH events. No duplicates in the answer.
#FIXME: Brute = compare every name on list 1 with every name on list 2.
#FIXME: Optimal = put list 1 into a lookup table, scan list 2 against it.
#FIXME:
#FIXME: Fun fact: Set intersection is the foundation of database JOINs.
#FIXME: When SQL does INNER JOIN, it's finding the "intersection" of two tables.


class Solution:
    #NOTE: Brute Force — O(n × m × r) time, O(r) space
    #TODO: For each element in nums1, check if it exists in nums2.
    #TODO: If found AND not already in result → add it.
    #TODO: `not in result` on a list is O(r) — makes it even slower.
    #TODO: Like cross-checking two attendance sheets name by name.
    def brute(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        for num1 in nums1:
            for num2 in nums2:
                if num1 == num2 and num1 not in result:
                    result.append(num1)
        return result

    #NOTE: Better — O(n + m) time, O(n) space (Manual HashSet approach)
    #TODO: Shows interviewer you understand HOW set intersection works internally.
    #TODO: Step 1: Put all of nums1 into a set (O(n), removes duplicates)
    #TODO: Step 2: For each element in nums2, check if in set1 (O(1) per check)
    #TODO: Step 3: Add to result set (auto-handles duplicates!)
    def better(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)  #NOTE: Convert to set — O(n), duplicates gone
        result = set()  #NOTE: Use set for result too — auto-prevents duplicates
        for num in nums2:
            if num in set1:  #NOTE: O(1) lookup — HashSet magic
                result.add(num)
        return list(result)

    #NOTE: Optimal — O(n + m) time, O(n + m) space (Pythonic one-liner)
    #TODO: set(nums1) & set(nums2) → Python's built-in set intersection
    #TODO: & on two sets returns a NEW set with only common elements
    def optimal(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2))  #NOTE: & = intersection. | = union. - = difference.


#NOTE: ===== PYTHON TIPS & BUILT-INS =====
#NOTE:
#NOTE: SET OPERATIONS (memorize these!):
#NOTE:   set(a) & set(b)  → Intersection (elements in BOTH)
#NOTE:   set(a) | set(b)  → Union (elements in EITHER)
#NOTE:   set(a) - set(b)  → Difference (in a but NOT in b)
#NOTE:   set(a) ^ set(b)  → Symmetric Difference (in one but NOT both)
#NOTE:
#NOTE: set.add(x)      → Add element (no duplicates ever, O(1))
#NOTE: x in my_set     → Check membership (O(1) — hash table lookup!)
#NOTE: set(list)       → Convert list to set (removes duplicates, O(n))
#NOTE: list(my_set)    → Convert set back to list
#NOTE:
#NOTE: HASHSET vs HASHMAP:
#NOTE:   HashMap (dict) = {key: value} → stores pairs (Two Sum: {num: index})
#NOTE:   HashSet (set)  = {key}        → stores only keys (Contains Duplicate: just existence)
#NOTE:   BOTH use hash tables internally → BOTH have O(1) lookup
#NOTE:   Rule: Need a VALUE with each key? → dict. Just need to check existence? → set.


if __name__ == "__main__":
    obj = Solution()

    # Case 1: Simple intersection
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print("Case 1:")
    print("  Brute:", obj.brute(nums1, nums2))      # [2]
    print("  Better:", obj.better(nums1, nums2))    # [2]
    print("  Optimal:", obj.optimal(nums1, nums2))  # [2]

    # Case 2: Multiple common elements
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print("\nCase 2:")
    print("  Brute:", obj.brute(nums1, nums2))      # [4, 9]
    print("  Better:", obj.better(nums1, nums2))    # [9, 4]
    print("  Optimal:", obj.optimal(nums1, nums2))  # [9, 4]

    # Case 3: No intersection
    nums1 = [1, 3, 5]
    nums2 = [2, 4, 6]
    print("\nCase 3:")
    print("  Brute:", obj.brute(nums1, nums2))      # []
    print("  Better:", obj.better(nums1, nums2))    # []
    print("  Optimal:", obj.optimal(nums1, nums2))  # []

    # Case 4: Identical arrays
    nums1 = [7, 7, 7]
    nums2 = [7, 7, 7]
    print("\nCase 4:")
    print("  Brute:", obj.brute(nums1, nums2))      # [7]
    print("  Better:", obj.better(nums1, nums2))    # [7]
    print("  Optimal:", obj.optimal(nums1, nums2))  # [7]

    # Case 5: One empty array
    nums1 = []
    nums2 = [1, 2, 3]
    print("\nCase 5:")
    print("  Brute:", obj.brute(nums1, nums2))      # []
    print("  Better:", obj.better(nums1, nums2))    # []
    print("  Optimal:", obj.optimal(nums1, nums2))  # []
