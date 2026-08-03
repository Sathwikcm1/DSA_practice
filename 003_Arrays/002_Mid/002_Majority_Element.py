#FIXME: Problem: Majority Element
#FIXME: Link: https://leetcode.com/problems/majority-element/
#FIXME: Given: An array `nums` of size n
#FIXME: Return: The element that appears more than ⌊n/2⌋ times
#FIXME: Constraints:
#FIXME:   - 1 <= n <= 5 * 10^4
#FIXME:   - -10^9 <= nums[i] <= 10^9
#FIXME:   - The majority element ALWAYS exists (guaranteed)
#FIXME:
#FIXME: Real-world scenario: Think of an election where one candidate gets MORE than
#FIXME: half the votes. You need to find WHO won. Brute = count each candidate's votes
#FIXME: manually. Optimal = tally sheet (HashMap) and stop the moment someone crosses 50%.
#FIXME:
#FIXME: Fun fact: Boyer-Moore Voting was invented in 1981. It finds the majority in a
#FIXME: STREAM of data using O(1) memory — meaning you could find the majority element
#FIXME: in a billion votes using just TWO variables. Used in real election systems.


class Solution:
    #NOTE: Brute Force — O(n²) time, O(1) space
    #TODO: For each element, count how many times it appears in the entire array.
    #TODO: If count > n/2 → that's our majority element.
    #TODO: Like counting raised hands for each candidate in a room, one by one.
    def brute(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n):
            cnt = 0
            for j in range(n):  #NOTE: Count occurrences across FULL array (not just i onwards)
                if nums[i] == nums[j]:
                    cnt += 1
            if cnt > n / 2:
                return nums[i]
        return -1

    #NOTE: Better/Optimal — O(n) time, O(n) space (HashMap counting)
    #TODO: Key Insight: Count frequency using HashMap. Return as soon as count > n//2.
    #TODO: Early exit = don't even finish counting. Like a live vote counter announcing
    #TODO: the winner the MOMENT someone crosses 50%, before all votes are tallied.
    def optimal(self, nums: list[int]) -> int:
        n = len(nums)
        hashmap = {}  #NOTE: {element: count}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1  #NOTE: .get(key, 0) + 1 → THE counting pattern
            if hashmap[num] > n // 2:  #NOTE: Early exit! No need to count everything.
                return num
        return -1

    #NOTE: BONUS — Boyer-Moore Voting Algorithm — O(n) time, O(1) space 🔥
    #TODO: THE legendary solution. No HashMap, no extra memory. Just 2 variables.
    #TODO: Intuition: Majority has MORE than n/2 elements. Even if every minority
    #TODO: element "cancels out" one majority element, majority STILL survives.
    #TODO: Think of a battle royale:
    #TODO:   - Pick a candidate, give them 1 life.
    #TODO:   - Same element? +1 life (ally arrived).
    #TODO:   - Different element? -1 life (enemy cancels one ally).
    #TODO:   - Lives hit 0? Old candidate dies. New one takes over.
    #TODO:   - The last candidate standing IS the majority (math guarantees it).
    def boyer_moore(self, nums: list[int]) -> int:
        candidate = nums[0]
        count = 0
        for num in nums:
            if count == 0:  #NOTE: Previous candidate fully cancelled → elect new one
                candidate = num
            if num == candidate:
                count += 1  #NOTE: Same as candidate → strengthen
            else:
                count -= 1  #NOTE: Different → cancel out one vote
        return candidate  #NOTE: Survivor = majority (guaranteed by problem)


#NOTE: ===== PYTHON TIPS & BUILT-INS =====
#NOTE: dict.get(key, default) → THE most important dict method for DSA!
#NOTE:   hashmap.get(num, 0) → "give me num's count, or 0 if never seen"
#NOTE:   hashmap.get(num, 0) + 1 → "increment count (starting from 0 if new)"
#NOTE:   This ONE pattern solves: Two Sum, Contains Duplicate, Valid Anagram, Majority Element
#NOTE:
#NOTE: Alternative using Counter:
#NOTE:   from collections import Counter
#NOTE:   return Counter(nums).most_common(1)[0][0]
#NOTE:
#NOTE: n // 2 vs n / 2:
#NOTE:   // = integer division (floor): 7//2 = 3
#NOTE:   /  = float division: 7/2 = 3.5
#NOTE:   For counting, use // (avoids float comparison weirdness)


if __name__ == "__main__":
    obj = Solution()

    # Case 1: Majority element exists
    nums = [3, 3, 4]
    print("Case 1 (Majority exists):")
    print("  Brute:", obj.brute(nums))              # 3
    print("  Optimal:", obj.optimal(nums))          # 3
    print("  Boyer-Moore:", obj.boyer_moore(nums))  # 3

    # Case 2: Classic example
    nums = [2, 2, 1, 1, 1, 2, 2]
    print("\nCase 2 (Classic):")
    print("  Brute:", obj.brute(nums))              # 2
    print("  Optimal:", obj.optimal(nums))          # 2
    print("  Boyer-Moore:", obj.boyer_moore(nums))  # 2

    # Case 3: No majority (edge case — problem guarantees it exists, but good to test)
    nums = [1, 2, 3, 4]
    print("\nCase 3 (No majority):")
    print("  Brute:", obj.brute(nums))              # -1
    print("  Optimal:", obj.optimal(nums))          # -1

    # Case 4: Single element
    nums = [7]
    print("\nCase 4 (Single):")
    print("  Brute:", obj.brute(nums))              # 7
    print("  Optimal:", obj.optimal(nums))          # 7
    print("  Boyer-Moore:", obj.boyer_moore(nums))  # 7

    # Case 5: All same
    nums = [9, 9, 9, 9, 9]
    print("\nCase 5 (All same):")
    print("  Brute:", obj.brute(nums))              # 9
    print("  Optimal:", obj.optimal(nums))          # 9
    print("  Boyer-Moore:", obj.boyer_moore(nums))  # 9
