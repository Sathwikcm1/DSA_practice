def brute_force_approach(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

def optimal_search(arr,target):
    low = 0
    high = len(arr - 1)
    while(low <= high):
        mid = (low+high)//2
        if arr[mid] == target :
            return mid
        #? this is if left part is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= target and target <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        #? this is if right part is sorted
        else:
            if arr[mid] <= target and target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

if __name__ == '__main__':
    arr = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(brute_force_approach(arr, target))