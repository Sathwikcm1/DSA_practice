#FIXME: Rotate the whole array left by one place. [1,2,3,4,5] → [2,3,4,5,1]
#* Pattern: Array Manipulation | Technique: In-place shift

class Solution:
    #TODO: Brute — Copy elements 1..n to temp array, place first element at end.
    #NOTE: Time: O(n) | Space: O(n) — extra array of size n-1
    def brute(self, arr: list[int]) -> None:
        n = len(arr)
        first_element = arr[0]
        temp_arr = []
        for i in range(1, n):
            temp_arr.append(arr[i])
        for i in range(len(temp_arr)):
            arr[i] = temp_arr[i]
        arr[n - 1] = first_element

    #TODO: Optimal — Save first, shift everything left by 1, place first at end.
    #NOTE: Time: O(n) | Space: O(1) — only 1 extra variable
    #NOTE: Both approaches are O(n) TIME — optimal is about SPACE.
    def optimal(self, arr: list[int]) -> None:
        first_element = arr[0]
        for i in range(1, len(arr)):
            arr[i - 1] = arr[i]
        arr[-1] = first_element

    #* Pythonic alternatives:
    #* arr[:] = arr[1:] + [arr[0]]      — slicing, O(n) space
    #* arr.append(arr.pop(0))            — pop(0) is O(n) internally
    #* deque(arr).rotate(-1)             — O(1) rotation if already a deque


def main():
    arr = [1, 2, 3, 4, 5, 6, 7]
    sol = Solution()
    sol.optimal(arr)
    for num in arr:
        print(num, end=" ")
    print()

main()
#NOTE: The time complexity of optimal is O(N.) single iteration. but the space complexity is improved.
#NOTE: SC : O(1).
