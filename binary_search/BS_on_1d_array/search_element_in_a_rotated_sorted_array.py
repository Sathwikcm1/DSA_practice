def brute_force_approach(arr,target): #? this is basically the brute force apporach where we just look for the target by going through the array.
    for i in range(len(arr)):  #? this loop will run till the length of the array
        if arr[i] == target:   #? if the target is found then it will return the index
            return i

def optimal_search(arr,target):  #todo this is the optimal approach, where we use binary search.
    low = 0
    high = len(arr - 1)
    while(low <= high):
        mid = (low+high)//2             #todo Calculating the mid index.
        if arr[mid] == target :         #todo if the target is found then it will return the index.
            return mid
        #? this is if left part is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= target and target <= arr[mid]:  #todo if the 
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