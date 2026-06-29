#FIXME: In the given array, every element is repeated twice except for one element, return it.
#* Pattern: XOR / Hashing | Technique: Frequency counting, XOR cancellation


class Solution:
    #TODO: Brute — For each element, count how many times it appears using nested loop.
    #NOTE: Outer loop picks element, inner loop counts occurrences. If count == 1, found it.
    #NOTE: Time: O(n²) | Space: O(1)
    #NOTE: ⚠️ LIMITATION: Extremely slow for large arrays. 10⁵ elements = 10¹⁰ operations.
    def brute(self, arr: list[int]) -> int:
        n = len(arr)
        if n % 2 == 0:
            return -1
        #NOTE: If array size is even, every element must appear twice — impossible to have a single one.
        for i in range(n):
            cnt = 0
            num = arr[i]
            for j in range(n):
                if arr[j] == num:
                    cnt += 1
            if cnt == 1:
                return num
        return -1

    #TODO: Better 1 — Hash Array. Create array of size max_val+1, use indices as keys.
    #NOTE: Time: O(n) | Space: O(max_val)
    #NOTE: ⚠️ LIMITATION: Only works with POSITIVE numbers (no negative indices).
    #NOTE: ⚠️ LIMITATION: Wastes space if max_val is huge (e.g., arr=[1, 999999] → allocates 1M slots).
    def hash_array(self, arr: list[int]) -> int:
        max_val = max(arr)
        hash_arr = [0] * (max_val + 1)
        for num in arr:
            hash_arr[num] += 1
        for i in range(len(hash_arr)):
            if hash_arr[i] == 1:
                return i
        return -1

    #TODO: Better 2 — HashMap (Dictionary). Flexible, works with negatives, strings, anything.
    #NOTE: freq.get(num, 0) is the Pythonic shortcut for the if/else check below.
    #NOTE: Counter(arr) from collections does the same thing in one line — interview flex.
    #NOTE: Time: O(n) | Space: O(n) — stores at most n/2 + 1 unique keys
    #NOTE: ⚠️ LIMITATION: Uses O(n) extra space unlike XOR which uses O(1).
    def hash_map(self, arr: list[int]) -> int:
        count: dict[int, int] = {}
        for num in arr:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        #NOTE: Pythonic alternative: count[num] = count.get(num, 0) + 1
        #NOTE: Even more Pythonic: from collections import Counter → count = Counter(arr)
        for num in count:
            if count[num] == 1:
                return num
        return -1

    #TODO: Optimal — XOR everything. Pairs cancel (a^a=0), the loner survives.
    #NOTE: Time: O(n) | Space: O(1) — no extra data structures at all.
    #NOTE: ⚠️ LIMITATION: Only works when every OTHER element appears EXACTLY twice.
    #NOTE: If elements appear 3 times or odd times, XOR won't isolate the single one.
    def optimal(self, arr: list[int]) -> int:
        xor = 0
        for num in arr:
            xor ^= num
        return xor


def main():
    arr = [1, 1, 2, 3, 3, 4, 5, 6, 5, 4, 6]
    sol = Solution()
    print("Brute:", sol.brute(arr))
    print("Hash Array:", sol.hash_array(arr))
    print("Hash Map:", sol.hash_map(arr))
    print("Optimal (XOR):", sol.optimal(arr))


main()
