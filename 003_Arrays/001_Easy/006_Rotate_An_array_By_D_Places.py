#FIXME: Rotate an array LEFT by "D" places. [1,2,3,4,5,6] d=3 → [4,5,6,1,2,3]
#* Pattern: Array Manipulation | Technique: Reversal Trick (Three Reversals)

class Solution:
    #TODO: Brute — Store first d elements in temp, shift rest left, place temp at end.
    #NOTE: d = d % n handles cases where d > array length (rotating by n = no change).
    #NOTE: Time: O(n) | Space: O(d) for temp array
    def brute(self, arr: list[int], d: int) -> None:
        n = len(arr)
        d = d % n
        temp_arr = []
        for i in range(d):
            temp_arr.append(arr[i])
        for i in range(d):
            arr[i] = arr[n - d + i]
        for i in range(len(temp_arr)):
            arr[d + i] = temp_arr[i]

    #NOTE: Helper — Reverse array between start and end indices (two-pointer swap)
    def reverse(self, arr: list[int], start: int, end: int) -> None:
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    #TODO: Optimal — Three reversals: reverse first d, reverse rest, reverse whole.
    #NOTE: Think of array as [A | B]. We want [B | A].
    #NOTE: Reverse A → A', Reverse B → B', Reverse(A'B') → [B | A] ✅
    #NOTE: Time: O(n) | Space: O(1) — purely in-place, no extra array
    def optimal(self, arr: list[int], d: int) -> None:
        n = len(arr)
        d = d % n
        if d == 0:
            return
        self.reverse(arr, 0, d - 1)
        self.reverse(arr, d, n - 1)
        self.reverse(arr, 0, n - 1)

    #* Pythonic alternative:
    #* arr[:] = arr[d:] + arr[:d]   — slicing, O(n) space


def main():
    arr = [1, 2, 3, 4, 5, 6]
    sol = Solution()

    sol.brute(arr, 3)
    print("Brute:", arr)

    arr2 = [1, 2, 3, 4, 5, 6]
    sol.optimal(arr2, 3)
    print("Optimal:", arr2)

main()
