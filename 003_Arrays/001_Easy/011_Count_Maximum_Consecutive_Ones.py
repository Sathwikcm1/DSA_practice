#FIXME: Count maximum consecutive ones in a binary array.
#* Pattern: Linear Scan | Technique: Running counter with reset
#NOTE: Example: [1,1,0,1,1,1] → output: 3 (three ones in a row)


class Solution:
    #TODO: Optimal — Single pass. Track current streak and max streak.
    #NOTE: If current element is 1 → increment counter. Otherwise → reset to 0.
    #NOTE: Update max after every increment. No need for separate comparison step.
    #NOTE: Time: O(n) | Space: O(1) — can't do better since you must see every element.
    def sol(self, arr: list[int]) -> int:
        cnt = 0
        largest_cnt = 0
        for num in arr:
            if num == 1:
                cnt += 1
                largest_cnt = max(largest_cnt, cnt)
            else:
                cnt = 0
        return largest_cnt


def main():
    arr = [1, 1, 1, 0, 1, 1]
    sol = Solution()
    print(f"Max consecutive ones: {sol.sol(arr)}")


main()
