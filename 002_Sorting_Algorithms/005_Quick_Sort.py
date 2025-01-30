#FIXME: This is Quick_sort, it selects a pivot element, and partitions the list into three parts, 
#elements less than pivot, equal to pivot, and then the elements greater than the pivot element.
#it recursively sorts the left and right partitions and combines them with the middle elements.

#NOTE: still not the best.

from typing import List
def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    pivot =  arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

#HACK: Time complexity : O(n logn ) for best and average case and for worst case it is O(n^2).

arr = [4,5,2,3,1]
arr = quick_sort(arr)
print(*arr)
