#FIXME: Find the missing number in unsorted array of numbers 1 to N.
#* Pattern: Math / XOR / Hashing | Technique: Sum formula, XOR cancellation


class Solution:
    #TODO: Brute — Sort the array, then check each number 1 to N.
    #NOTE: Sorting uses Timsort (derived from merge sort) → O(n log n).
    #NOTE: Then `i not in arr` is O(n) per check → total O(n²) worst case.
    #NOTE: Edge cases: check if 1 is missing (start) or N is missing (end) first.
    #NOTE: Time: O(n log n) + O(n²) | Space: O(1)
    def brute(self, arr: list[int]) -> int:
        n = len(arr) + 1
        arr.sort()
        for i in range(1, n + 1):
            if i not in arr:
                return i
        return -1

    #TODO: Better — XOR all numbers 1..N, XOR all elements in arr, XOR results.
    #NOTE: firstly you are not vegeta! jk, XOR magic: a ^ a = 0, a ^ 0 = a.
    #NOTE: Matching numbers cancel out, only the missing one survives.
    #NOTE: Like a light switch — flip twice (same number) = OFF. Flip once (missing) = ON.
    #NOTE: No overflow risk unlike sum formula — XOR stays within bit width.
    #NOTE: Time: O(n) | Space: O(1)
    def better(self, arr: list[int]) -> int:
        n = len(arr) + 1
        xor1 = 0
        #NOTE: XOR all numbers from 1 to N (the complete range)
        for i in range(1, n + 1):
            xor1 ^= i
        xor2 = 0
        #NOTE: XOR all elements in the array (missing one number)
        for num in arr:
            xor2 ^= num
        #NOTE: XOR of both — matching pairs cancel to 0, missing number remains.
        return xor1 ^ xor2

    #TODO: Optimal — Using the power of friendship, Nah using meth... MATH*.
    #NOTE: Sum of 1 to N = N*(N+1)//2. Subtract actual array sum → missing number.
    #NOTE: Pythonic: sum(arr) instead of manual loop.
    #NOTE: Time: O(n) | Space: O(1)
    def optimal(self, arr: list[int]) -> int:
        n = len(arr) + 1
        total_sum = n * (n + 1) // 2
        arr_sum = sum(arr)
        return total_sum - arr_sum


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 9, 10]
    h = Solution()
    missing_number = h.brute(arr)
    print(f"The missing number from the array: {missing_number}")

    arr2 = [1, 2, 3, 4, 5, 6, 7, 9, 10]
    mis_num = h.optimal(arr2)
    print(f"The missing number from optimal method: {mis_num}")

    #NOTE: mew uses better. woof is the answer. meow. 🐱
    mew = Solution()
    woof = mew.better(arr2)
    print(f"The miss: {woof}")


main()
