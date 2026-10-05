## Reverse a Number

### Problem Statement

Reverse the digits of a given integer (handle negative numbers).

```python
def reverse_Num(n):
    rev_no = 0
    if n < 0:
        return -reverse_Num(-n)
    while n:
        ld = n % 10
        rev_no = rev_no * 10 + ld
        n = n//10
    return rev_no if rev_no <= 0x7fffffff else 0
```

**Explanation:**

- Convert negative to positive, reverse it, and then reapply `-`.
    
- `%` gets the last digit.
    
- `rev_no * 10 + ld` builds the reversed number.
    
- Handles overflow for 32-bit int.
    

> [!summary] Reverse a Number  
> Uses modulus and integer division. Recursive handling for negative input. Overflow condition check.

> [!TIP]  
> Check overflow and negatives **before** reversing.

---

## Bubble Sort

### Problem Statement

Sort an array using Bubble Sort. Compare and swap adjacent elements if they're in the wrong order.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print("This is using bubble sort:")
    for num in arr:
        print(num, end=" ")
    print()
```

**Explanation:**

- Largest element "bubbles" to the end in each pass.
    
- On `i`th iteration, last `i` elements are sorted.
    
- Best case is O(n) if array is sorted; worst/avg is O(n²).
    

> [!summary] Bubble Sort  
> Repeatedly swap adjacent elements. Good for small or nearly sorted arrays.

> [!TIP]  
> Early exit optimization (check if no swaps happened) can improve best-case performance.

---

## Selection Sort

### Problem Statement

Select the smallest element from unsorted part and move to sorted region.

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        mini = i
        for j in range(i+1, n):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]
```

**Explanation:**

- Outer loop runs `n-1` times.
    
- For each index `i`, find min element in remaining array.
    
- Place that min element at position `i`.
    

> [!summary] Selection Sort  
> Always O(n²). Useful when memory writes are costly.

> [!TIP]  
> Selection sort makes the minimum number of swaps among basic sorts.

---

## Insertion Sort

### Problem Statement

Build a sorted array one element at a time by inserting unsorted items into correct position.

```python
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
```

**Explanation:**

- Start from index 1, compare and insert element into sorted left portion.
    
- Best case O(n) when array is already sorted.
    
- Worst and avg: O(n²).
    

> [!summary] Insertion Sort  
> Efficient for nearly sorted data. In-place and stable.

> [!TIP]  
> Great for small datasets or almost sorted arrays.

---

## Merge Sort

### Problem Statement

Sort the array using Divide and Conquer (merge sort).

```python
def merge_sort(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)
    merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    left = low
    right = mid + 1
    temp = []

    while left <= mid and right <= high:
        if arr[left] < arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(low, high + 1):
        arr[i] = temp[i - low]
```

**Explanation:**

- Recursively split array till size 1, then merge.
    
- Merge two sorted arrays into one.
    
- Time complexity: O(n log n) for all cases.
    

> [!summary] Merge Sort  
> Divide, conquer, and merge. Time complexity always O(n log n).

> [!TIP]  
> Preferred for large datasets and guaranteed performance.

---

## Quick Sort

### Problem Statement

Sort the array by choosing a pivot and partitioning the array around the pivot.

```python
from typing import List

def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

**Explanation:**

- Choose pivot (here: middle element).
    
- Partition into left (< pivot), middle (= pivot), right (> pivot).
    
- Recursively sort left and right.
    
- Best/avg case O(n log n); worst case O(n²).
    

> [!summary] Quick Sort  
> Fast in practice. Divide and conquer using pivot partitioning.

> [!TIP]  
> Randomized or median pivot can help avoid worst-case performance.

---