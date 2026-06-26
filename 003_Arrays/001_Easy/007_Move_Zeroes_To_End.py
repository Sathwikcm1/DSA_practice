#FIXME: Move all zeroes to the end of the array. [1,0,2,0,3] → [1,2,3,0,0]
#* Pattern: Two Pointers | Technique: Snowball / Partition swap


class Solution:
    #TODO: Brute — Collect non-zeroes into temp, pad with zeroes, copy back.
    #NOTE: Think of it like taking all books off a shelf, removing empty slots,
    #NOTE: then placing books back and filling remaining slots with blanks.
    #NOTE: Time: O(n) | Space: O(n) — temp_arr can hold up to n elements
    def brute(self, arr: list[int]) -> None:
        if not arr:
            return None
        temp_arr = []
        for num in arr:
            if num != 0:
                temp_arr.append(num)

        temp_arr_len = len(temp_arr)
        addzero = len(arr) - temp_arr_len

        for i in range(addzero):
            temp_arr.append(0)

        #NOTE: Instead of the above for loop we can also do this:
        #NOTE: temp_arr += [0] * addzero — creates a list of zeros and extends.

        for i in range(len(arr)):
            arr[i] = temp_arr[i]

    #TODO: Optimal — Two pointer swap. j = leftmost zero, i = scanner.
    #NOTE: j always points to the leftmost zero (the slot where next non-zero should go).
    #NOTE: When we swap a non-zero into j's position, j advances — zeros accumulate at end.
    #NOTE: Like OS memory compaction: active blocks move left, free space collects at the end.
    #NOTE: Time: O(n) | Space: O(1) — no extra array, purely in-place swaps
    def optimal(self, arr: list[int]) -> None:
        j = -1
        #NOTE: Step 1 — Find the index of the FIRST zero. break immediately.
        for i in range(len(arr)):
            if arr[i] == 0:
                j = i
                break
        #NOTE: If j is still -1, no zeros exist in the array — nothing to move.
        if j == -1:
            return
        #NOTE: Step 2 — Scan from j+1. Every non-zero swaps with arr[j], then j advances.
        for i in range(j + 1, len(arr)):
            if arr[i] != 0:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1


def main():
    arr = [1, 2, 3, 4, 5, 12, 0, -12, -121, 0, 23, 0, 0, 1]
    sol = Solution()

    sol.brute(arr)
    print("Brute:", arr)

    arr2 = [1, 2, 3, 4, 5, 12, 0, -12, -121, 0, 23, 0, 0, 1]
    sol.optimal(arr2)
    print("Optimal:", arr2)


main()
