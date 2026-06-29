#FIXME: Find the longest subarray whose elements sum to K.
#* Pattern: Prefix Sum + HashMap / Sliding Window
#NOTE: Example: arr=[2,3,5,1,9], K=10 → answer: 3 (subarray [2,3,5] has sum 10, length 3)


class Solution:
    #TODO: Brute — Try every possible subarray using two nested loops.
    #NOTE: Outer loop = start index, inner loop = end index. Accumulate sum as j moves.
    #NOTE: No need for a third loop — add arr[j] to running sum inside inner loop.
    #NOTE: Time: O(n²) | Space: O(1)
    def brute(self, arr: list[int], k: int) -> int:
        n = len(arr)
        max_len = 0
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += arr[j]
                if current_sum == k:
                    max_len = max(max_len, j - i + 1)
        return max_len

    #TODO: Better — Prefix Sum + HashMap. O(n) time, O(n) space.
    #NOTE: Core idea: if prefix_sum[j] - prefix_sum[i] == K, then subarray (i+1 to j) sums to K.
    #NOTE: Store {prefix_sum: first_index_where_this_sum_occurred} in a dict.
    #NOTE: At each index, check if (prefix_sum - K) exists in the map.
    #NOTE: Only store prefix_sum if NOT already in map (keep earliest index for longest subarray).
    #NOTE: Works with BOTH positive AND negative numbers. This is the real optimal for mixed arrays.
    def better(self, arr: list[int], k: int) -> int:
        n = len(arr)
        prefix_sum_map: dict[int, int] = {}
        prefix_sum = 0
        max_len = 0

        for i in range(n):
            prefix_sum += arr[i]

            #NOTE: If prefix_sum itself equals K, the subarray is arr[0..i], length = i+1.
            if prefix_sum == k:
                max_len = max(max_len, i + 1)

            #NOTE: Check if (prefix_sum - K) was seen before.
            #NOTE: If yes, the subarray from that index+1 to current i has sum K.
            remainder = prefix_sum - k
            if remainder in prefix_sum_map:
                length = i - prefix_sum_map[remainder]
                max_len = max(max_len, length)

            #NOTE: Store prefix_sum with its index — but ONLY if not already stored.
            #NOTE: We keep the earliest index to maximize subarray length.
            if prefix_sum not in prefix_sum_map:
                prefix_sum_map[prefix_sum] = i

        return max_len

    #TODO: Optimal — Sliding Window (Two Pointers). O(n) time, O(1) space.
    #NOTE: ONLY WORKS WITH POSITIVE NUMBERS. Negatives break the window logic.
    #NOTE: Expand window (right++) to increase sum. Shrink window (left++) to decrease sum.
    #NOTE: When sum == K, record the window length.
    def optimal(self, arr: list[int], k: int) -> int:
        n = len(arr)
        left, right = 0, 0
        current_sum = arr[0]
        max_len = 0

        while right < n:
            #NOTE: Shrink window from left while sum exceeds K.
            while left <= right and current_sum > k:
                current_sum -= arr[left]
                left += 1

            #NOTE: Check if current window sums to K.
            if current_sum == k:
                max_len = max(max_len, right - left + 1)

            #NOTE: Expand window to the right.
            right += 1
            if right < n:
                current_sum += arr[right]

        return max_len


def main():
    arr = [2, 3, 5, 1, 9]
    k = 10
    sol = Solution()

    print(f"Brute: {sol.brute(arr, k)}")
    print(f"Better (HashMap): {sol.better(arr, k)}")
    print(f"Optimal (Sliding Window): {sol.optimal(arr, k)}")


main()
