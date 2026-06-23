#FIXME: Remove the repeated elements from a sorted array.
#* Pattern: Two Pointers | Technique: Slow-Fast pointer on sorted data

class Solution:
    #TODO: Brute — Use set to eliminate duplicates, copy back to array.
    #NOTE: set() removes duplicates but does NOT preserve order.
    #NOTE: Pythonic shortcut: st = set(arr) — no need for manual loop.
    #NOTE: Time: O(n) for set + O(n) copy = O(n) | Space: O(n) for the set
    def brute(self, arr: list[int]) -> int:
        st = set(arr)
        j = 0
        for x in sorted(st):
            arr[j] = x
            j += 1
        return len(st)

    #TODO: Optimal — Two pointers on sorted array. i = last unique, j = scanner.
    #NOTE: Since array is SORTED, duplicates are adjacent. If arr[j] != arr[i], it's a new unique.
    #NOTE: arr[i] = arr[j] places the new unique right after the last one. Builds unique section in-place.
    #NOTE: Time: O(n) | Space: O(1) — no extra data structure needed.
    def optimal(self, arr: list[int]) -> int:
        i = 0
        for j in range(1, len(arr)):
            if arr[i] != arr[j]:
                i += 1
                arr[i] = arr[j]
        return i + 1


def main():
    arr = [1, 1, 23, 4, 4, 23, 34, 0, -12, -234, 29]
    sol = Solution()

    #NOTE: Problem requires SORTED array — sort first!
    arr.sort()
    print("Sorted array:", arr)

    k = sol.optimal(arr)
    print("After removing duplicates:")
    for i in range(k):
        print(arr[i], end=" ")
    print()

main()
