#FIXME: Find the second largest number in the array.
#* Pattern: Linear Scan | Technique: Single Pass with Two Trackers

class Solution:
    #TODO: Brute — Find max first using max(), then scan for the largest element that isn't max.
    #NOTE: Two passes: max() is O(n) + loop is O(n) = O(2n) → effectively O(n).
    #NOTE: This is technically the "better" approach. True brute would sort first → O(n log n).
    #NOTE: Edge case: len < 2 → no second largest exists, return None.
    def brute(self, arr: list[int]) -> int | None:
        if len(arr) < 2:
            return None
        second_largest = float('-inf')
        largest = max(arr)

        for num in arr:
            if num > second_largest and num != largest:
                second_largest = num
        return second_largest

    #TODO: Optimal — Single pass, track both largest and second_largest simultaneously.
    #NOTE: Key insight: when a new largest is found, the OLD largest becomes second_largest.
    #NOTE: elif (not if!) — once we update largest, we STOP. Don't also check second condition.
    #NOTE: Time: O(n) | Space: O(1)
    def optimal(self, arr: list[int]) -> int | None:
        if len(arr) < 2:
            return None
        largest = second_largest = float('-inf')
        for num in arr:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num != largest:
                second_largest = num
        return second_largest


def main():
    arr = [5, 3, 5, 6, -1, 34, 0, 3434]
    sol = Solution()
    print("Brute:", sol.brute(arr))
    print("Optimal:", sol.optimal(arr))

main()

