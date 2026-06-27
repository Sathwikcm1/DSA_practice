#FIXME: Linear search — go through the array to find a given element.
#* Pattern: Linear Scan | Technique: Sequential search
#NOTE: Time: O(n) | Space: O(1) — worst case checks every element once.


class Solution:
    #TODO: Pythonic — `in` operator does linear search internally, returns True/False.
    #NOTE: Under the hood, Python's `in` iterates through the list — it IS linear search.
    #NOTE: Use this when you only need existence check, not the index.
    def brute(self, arr: list[int], k: int) -> bool:
        return k in arr

    #TODO: Optimal (Interview version) — explicit loop, returns INDEX or -1 if not found.
    #NOTE: enumerate() gives (index, value) pairs — avoids manual arr[i] indexing.
    #NOTE: Time: O(n) | Space: O(1)
    def optimal(self, arr: list[int], k: int) -> int:
        for i, num in enumerate(arr):
            if num == k:
                return i
        return -1


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 10, -12, -1212]
    sol = Solution()
    print("Brute (exists?):", sol.brute(arr, 7))
    print("Optimal (index):", sol.optimal(arr, -12))


main()
