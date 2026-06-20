#FIXME: Find the largest number in an array.
#* Pattern: Linear Scan | Technique: Sorting / Single Pass

class Solution:
    #TODO: Brute — Sort the array, last element is the largest.
    #NOTE: sorted() returns a NEW sorted list (original untouched). O(n) extra space.
    #NOTE: arr.sort() sorts IN-PLACE (modifies original). O(1) extra space. 
    #NOTE: Time: O(n log n) | Space: O(n) because of sorted()
    def brute(self, arr: list[int]) -> int:
        return sorted(arr)[-1]
    
    #TODO: Optimal — Single pass, track the largest seen so far.
    #NOTE: float('-inf') handles all-negative arrays. Using 0 would FAIL for [-5, -3, -1].
    #NOTE: Time: O(n) | Space: O(1)
    def optimal(self, arr: list[int]) -> int:
        largest = float('-inf')
        for num in arr:
            if num > largest:
                largest = num
        return largest

    #* Python shortcut: max(arr) does exactly what optimal() does. O(n) time.
    #! Important: max(arr) returns the same thing in the same time. 

def main():
    arr = [-121, 23, -12, 3, 2, 4, 34, 3434, 3434, 0, 10000]
    s = Solution()

    print("Brute:", s.brute(arr))
    print("Optimal:", s.optimal(arr))
    print("Built-in:", max(arr))   #NOTE: Pythonic way — use max() in real code

main()
