#FIXME: Find the second largest number present in the given array.

def brute_force(arr):
    largest = float('-inf')
    s_largest = float('-inf')

    for num in arr:
        largest = max(num,largest)
    arr.sort()

    for i in range(len(arr) - 2, -1 , -1):
        if arr[i] != largest:
            s_largest = arr[i]
            break
    return s_largest

def better(arr):
    largest = float('-inf')
    s_largest = float('-inf')

    for num in arr:
        largest = max(num,largest)

    for num in arr:
        if num > s_largest and num != largest:
            s_largest = num
    return s_largest
