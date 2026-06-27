#FIXME: Union of two sorted arrays — result should contain all unique elements from both.
#* Pattern: Two Pointers (merge) | Also: Set / Dict approaches


class Solution:
    #TODO: Brute — Use set union. Handles unsorted arrays too.
    #NOTE: set() removes duplicates, | operator combines both sets.
    #NOTE: Time: O(n + m) | Space: O(n + m) for the set
    def brute(self, arr1: list[int], arr2: list[int]) -> list[int]:
        return sorted(set(arr1) | set(arr2))

    #TODO: Better — Use dictionary to count, then extract keys.
    #NOTE: dict.get(key, default) returns default if key missing — avoids KeyError.
    #NOTE: We only care about keys (unique elements), values (counts) are irrelevant for union.
    #NOTE: Time: O(n + m) | Space: O(n + m)
    def better(self, arr1: list[int], arr2: list[int]) -> list[int]:
        freq: dict[int, int] = {}
        for num in arr1:
            freq[num] = freq.get(num, 0) + 1
        for num in arr2:
            freq[num] = freq.get(num, 0) + 1
        return sorted(freq.keys())

    #TODO: Optimal — Two pointer merge on SORTED arrays. No hashing needed.
    #NOTE: Both arrays MUST be sorted for this to work!
    #NOTE: Walk two pointers like a zipper — smaller element goes first.
    #NOTE: Skip duplicates by checking if union[-1] == current element.
    #NOTE: After one array is exhausted, drain the other.
    #NOTE: Time: O(n + m) | Space: O(n + m) for the result array only
    def optimal(self, arr1: list[int], arr2: list[int]) -> list[int]:
        union: list[int] = []
        i, j = 0, 0

        #NOTE: Main merge — compare arr1[i] vs arr2[j], pick the smaller one.
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                if not union or union[-1] != arr1[i]:
                    union.append(arr1[i])
                i += 1
            else:
                if not union or union[-1] != arr2[j]:
                    union.append(arr2[j])
                j += 1

        #NOTE: Drain remaining elements from arr1 (if arr2 finished first)
        while i < len(arr1):
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1

        #NOTE: Drain remaining elements from arr2 (if arr1 finished first)
        while j < len(arr2):
            if not union or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1

        return union


def main():
    arr1 = [1, 2, 3, 4, 5, 6, 6, 7]
    arr2 = [0, 1, 2, 3, 4, 8, 9]

    sol = Solution()
    print("Brute:", sol.brute(arr1, arr2))
    print("Better:", sol.better(arr1, arr2))
    print("Optimal:", sol.optimal(arr1, arr2))


main()
