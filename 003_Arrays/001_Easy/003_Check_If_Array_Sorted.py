#FIXME: Check if the array is sorted (non-decreasing order).
#* Pattern: Linear Scan | Technique: Adjacent Pair Comparison

class Solution:
    #TODO: Brute — Sort a copy and compare with original.
    #NOTE: sorted() creates a new sorted list, == compares element-by-element.
    #NOTE: Time: O(n log n) | Space: O(n)
    def brute(self, arr: list[int]) -> bool:
        return sorted(arr) == arr

    #TODO: Optimal — Single pass, check every adjacent pair.
    #NOTE: If any arr[i] > arr[i+1], array is NOT sorted → return False immediately.
    #NOTE: range(len(arr)-1) ensures i+1 is always in bounds. No modulo needed.
    #NOTE: Time: O(n) | Space: O(1)
    def optimal(self, arr: list[int]) -> bool:
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True


def main():
    arr = [1, 2, 3, 4, 5]
    sol = Solution()
    print("Brute:", sol.brute(arr))
    print("Optimal:", sol.optimal(arr))

main()
